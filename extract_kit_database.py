import pypdf
import re
import json

def extract_and_compile():
    print("Loading PDF...")
    reader = pypdf.PdfReader('TX_Exam_Kit_FA25.pdf')
    total_pages = len(reader.pages)
    print(f"Loaded {total_pages} pages.")

    # 1. EXTRACT QUESTIONS TEXT
    print("Extracting questions text...")
    questions_text = ""
    # Section 1 to 5 questions are from physical page 1 to 210
    # In 0-indexed terms, this is from page 46 to 255
    for p in range(46, 256):
        questions_text += f"\n--- PAGE {p+1} ---\n" + reader.pages[p].extract_text() + "\n"

    # 2. EXTRACT ANSWERS TEXT
    print("Extracting answers text...")
    answers_text = ""
    # Section 6 to 10 answers are from physical page 211 to 608
    # In 0-indexed terms, this is from page 256 to 608
    for p in range(256, 609):
        answers_text += f"\n--- PAGE {p+1} ---\n" + reader.pages[p].extract_text() + "\n"

    # 3. PARSE ANSWERS
    print("Parsing answer keys and workings...")
    # Find answer letter keys like "3 C", "15 A", "128 B", etc.
    # The pattern should find a number at the start of a line or after a page break, followed by a letter A-D
    ans_map = {}
    
    # We find all matching lines in answers_text
    # Answers typically start with something like "\n3 C\n" or "\n3 C   \n" or "\n15 A\n"
    # Let's write a regex to find all instances
    ans_pattern = re.compile(r'\n(\d+)\s+([A-D])\b')
    for m in ans_pattern.finditer(answers_text):
        num = int(m.group(1))
        letter = m.group(2)
        if num not in ans_map:
            ans_map[num] = {"letter": letter, "page_start": answers_text.count("\n", 0, m.start())}

    # Now let's extract the detailed workings for each answer
    # The working starts right after the answer key and goes until the next answer key or heading
    ans_keys = sorted(ans_map.keys())
    for i in range(len(ans_keys)):
        num = ans_keys[i]
        start_pos = answers_text.find(f"\n{num} {ans_map[num]['letter']}")
        if start_pos == -1:
            # try with space/tabs
            start_pos = answers_text.find(f"\n{num}\t{ans_map[num]['letter']}")
        
        if start_pos != -1:
            # The end of this answer's working is the start of the next answer
            if i < len(ans_keys) - 1:
                next_num = ans_keys[i+1]
                next_letter = ans_map[next_num]['letter']
                end_pos = answers_text.find(f"\n{next_num} {next_letter}", start_pos + 5)
                if end_pos == -1:
                    end_pos = answers_text.find(f"\n{next_num}\t{next_letter}", start_pos + 5)
            else:
                end_pos = len(answers_text)

            if end_pos != -1:
                working = answers_text[start_pos:end_pos].strip()
                # Clean working text
                ans_map[num]["working"] = working
            else:
                ans_map[num]["working"] = "Detailed working is provided in the official Kaplan Exam Kit."
        else:
            ans_map[num]["working"] = "Detailed working is provided in the official Kaplan Exam Kit."

    print(f"✓ Parsed {len(ans_map)} answer keys and workings.")

    # 4. PARSE QUESTIONS
    print("Parsing questions text...")
    parsed_questions = []

    # For each question in our answer map, let's locate it in the questions_text
    for num in sorted(ans_map.keys()):
        # Find where physical question starts in questions_text
        # Questions typically start with "\n<num> " or "\n<num>\n" or similar
        start_q = questions_text.find(f"\n{num} ")
        if start_q == -1:
            start_q = questions_text.find(f"\n{num}\n")
        
        if start_q != -1:
            # Find the end of this question, which is the start of the next question
            # We look for next question number like "\n<num+1> " or "\n<num+1>\n"
            # Let's try to find any number "\n<next_num> "
            next_q = -1
            # We can find the next integer in the sorted keys list
            curr_idx = sorted(ans_map.keys()).index(num)
            if curr_idx < len(ans_map.keys()) - 1:
                next_num = sorted(ans_map.keys())[curr_idx+1]
                next_q = questions_text.find(f"\n{next_num} ", start_q + 5)
                if next_q == -1:
                    next_q = questions_text.find(f"\n{next_num}\n", start_q + 5)
            
            if next_q != -1:
                q_body = questions_text[start_q:next_q].strip()
            else:
                # Limit to 2000 chars or until next major break
                q_body = questions_text[start_q:start_q+2000].strip()

            # Clean and parse question text
            # Options typically look like: "A ...", "B ...", "C ...", "D ..." on lines
            options = []
            opt_a_idx = q_body.find("\nA ")
            if opt_a_idx == -1: opt_a_idx = q_body.find("\nA\n")
            
            opt_b_idx = q_body.find("\nB ")
            if opt_b_idx == -1: opt_b_idx = q_body.find("\nB\n")
            
            opt_c_idx = q_body.find("\nC ")
            if opt_c_idx == -1: opt_c_idx = q_body.find("\nC\n")
            
            opt_d_idx = q_body.find("\nD ")
            if opt_d_idx == -1: opt_d_idx = q_body.find("\nD\n")

            if opt_a_idx != -1 and opt_b_idx != -1 and opt_c_idx != -1 and opt_d_idx != -1:
                # We have options!
                q_text = q_body[:opt_a_idx].strip()
                opt_a = q_body[opt_a_idx:opt_b_idx].strip()[2:].strip()
                opt_b = q_body[opt_b_idx:opt_c_idx].strip()[2:].strip()
                opt_c = q_body[opt_c_idx:opt_d_idx].strip()[2:].strip()
                opt_d = q_body[opt_d_idx:].strip()[2:].strip()
                # Remove page numbers or header artifacts from options
                options = [opt_a, opt_b, opt_c, opt_d]
            else:
                q_text = q_body
                options = []

            # Clean q_text by removing the leading number
            q_text_cleaned = re.sub(r'^\d+\s+', '', q_text)
            # Remove page markers like "--- PAGE \d+ ---"
            q_text_cleaned = re.sub(r'--- PAGE \d+ ---', '', q_text_cleaned)
            q_text_cleaned = re.sub(r'TX–UK: TAXATION.*?\n', '', q_text_cleaned, flags=re.I)
            q_text_cleaned = re.sub(r'KAPLAN PUBLISHING.*?\n', '', q_text_cleaned, flags=re.I)

            # Store the compiled question
            parsed_questions.append({
                "num": num,
                "text": q_text_cleaned.strip(),
                "options": options,
                "letter": ans_map[num]["letter"],
                "working": ans_map[num]["working"]
            })

    print(f"✓ Compiled {len(parsed_questions)} questions with options.")
    
    # Save to json file for reference or script usage
    with open('compiled_questions.json', 'w', encoding='utf-8') as f:
        json.dump(parsed_questions, f, indent=2)
    print("Saved compiled_questions.json")

if __name__ == '__main__':
    extract_and_compile()
