import re, sys
import pypdf

def audit():
    print("Reading TX-UK_Revision_Pack.html...")
    with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
        html = f.read()

    print("Reading TX_Exam_Kit_FA25.pdf...")
    reader = pypdf.PdfReader('TX_Exam_Kit_FA25.pdf')

    errors = []

    # PASS 1: Structural Integrity
    # Check parts 1 to 100
    part_markers = [int(x) for x in re.findall(r'<!-- ═══ PART (\d+)/100', html)]
    part_set = set(part_markers)
    missing_parts = [i for i in range(1, 101) if i not in part_set]
    if missing_parts:
        errors.append({
            'severity': 'CRITICAL',
            'part': 'Structural',
            'location': 'Part Markers',
            'issue': f'Missing part markers: {missing_parts}',
            'doc_says': f'Found parts: {sorted(list(part_set))}',
            'kit_says': 'All 100 parts must be present',
            'fix': f'Add missing parts: {missing_parts}'
        })

    # Check head/body/style tag counts
    heads = len(re.findall(r'<head\b', html, re.I))
    bodies = len(re.findall(r'<body\b', html, re.I))
    styles = len(re.findall(r'<style\b', html, re.I))

    if heads != 1 or bodies != 1 or styles != 1:
        errors.append({
            'severity': 'HIGH',
            'part': 'Structural',
            'location': 'DOM Tag Structure',
            'issue': f'Tag count mismatch: <head>={heads}, <body>={bodies}, <style>={styles}',
            'doc_says': f'Heads: {heads}, Bodies: {bodies}, Styles: {styles}',
            'kit_says': 'Exactly one <head>, <body>, and <style> tag',
            'fix': 'Ensure single <head>, <body>, and <style> tags'
        })

    # Check duplicate element IDs
    ids = re.findall(r'id=["\']([^"\']+)["\']', html)
    id_counts = {}
    for i in ids:
        id_counts[i] = id_counts.get(i, 0) + 1
    dup_ids = [i for i, count in id_counts.items() if count > 1]
    if dup_ids:
        errors.append({
            'severity': 'MEDIUM',
            'part': 'Structural',
            'location': 'HTML IDs',
            'issue': f'Duplicate element IDs found: {dup_ids}',
            'doc_says': f'Duplicates: {dup_ids}',
            'kit_says': 'All element IDs must be unique',
            'fix': 'Deduplicate element IDs'
        })

    # PASS 2: Rates & Allowances Verification against PDF pp 37-46
    # PDF page 37 is index 36
    rates_text = ""
    for p in range(36, 46):
        rates_text += reader.pages[p].extract_text() + "\n"

    # Rate checks in doc
    # Check van fuel scale charge in doc: £769 vs £757? Let's check kit!
    kit_van_fuel = "757" if "757" in rates_text or "van fuel benefit" in rates_text.lower() else "unknown"
    # Let's search van fuel in rates_text:
    for line in rates_text.split('\n'):
        if 'van' in line.lower() or 'fuel' in line.lower() or 'marginal' in line.lower() or 'fraction' in line.lower():
            print("Kit Rate Line:", line)

    # Let's verify specific numbers in html:
    # 1. Van fuel scale charge
    if "769" in html and "757" in rates_text:
        errors.append({
            'severity': 'HIGH',
            'part': 'Part 12',
            'location': 'IT-06 Van Fuel Scale Charge',
            'issue': 'Van fuel scale charge mismatch',
            'doc_says': 'Van fuel scale charge = £769 or £757',
            'kit_says': 'Van fuel scale charge = £757 (p.38)',
            'fix': 'Ensure van fuel scale charge is £757'
        })

    # PASS 3: Calculation Recomputation
    # Let's check Q19 lease premium formula in Part 21
    # Document says: £82,000 × (50 - 14)/50 = £59,040.
    # Formula in kit p.11: Premium × [51 - (N - 1)] / 50 = £82,000 × (51 - 14) / 50 = £82,000 × 37 / 50 = £60,680!
    # Let's check answer 19 in kit!
    a19_text = reader.pages[263].extract_text() # approx answer 19
    for p in range(256, 270):
        t = reader.pages[p].extract_text()
        if '19 A' in t or '19 B' in t or '19 C' in t or '19 D' in t or '59,040' in t or '60,680' in t:
            print(f'Answer 19 found on PDF p.{p+1}:')
            print(t[:400])

    print("Audit run complete. Errors found:", len(errors))
    for e in errors:
        print(f"[{e['severity']}] {e['part']} - {e['issue']}")

if __name__ == '__main__':
    audit()
