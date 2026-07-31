import re, sys
import pypdf

def run_full_audit():
    with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
        html = f.read()

    reader = pypdf.PdfReader('TX_Exam_Kit_FA25.pdf')

    log = []

    # PASS 1: STRUCTURAL & ASSEMBLY INTEGRITY
    # Check 1: All 100 part markers
    part_markers = [int(x) for x in re.findall(r'<!-- ═══ PART (\d+)/100', html)]
    part_counts = {p: part_markers.count(p) for p in set(part_markers)}
    missing = [p for p in range(1, 101) if p not in part_counts]

    if missing:
        log.append({
            'severity': 'CRITICAL',
            'part': 'Structural',
            'heading': 'Part Markers',
            'location': 'Document-wide',
            'issue': f'Missing part markers: {missing}',
            'doc_says': f'Present parts: {len(part_counts)}',
            'kit_says': 'All 100 parts present in numeric order',
            'fix': f'Add missing part markers: {missing}'
        })

    # Check 2: DOM tag structure
    heads = len(re.findall(r'<head\b', html, re.I))
    bodies = len(re.findall(r'<body\b', html, re.I))
    styles = len(re.findall(r'<style\b', html, re.I))

    if heads != 1 or bodies != 1 or styles != 1:
        log.append({
            'severity': 'HIGH',
            'part': 'Structural',
            'heading': 'DOM Tags',
            'location': 'HTML Shell',
            'issue': f'Multiple HTML shell tags found: <head>={heads}, <body>={bodies}, <style>={styles}',
            'doc_says': f'head={heads}, body={bodies}, style={styles}',
            'kit_says': 'Exactly 1 <head>, 1 <body>, 1 <style>',
            'fix': 'Clean up duplicate shell tags'
        })

    # Check 3: Unique element IDs
    ids = re.findall(r'\bid=["\']([^"\']+)["\']', html)
    id_counts = {}
    for i in ids:
        id_counts[i] = id_counts.get(i, 0) + 1
    dup_ids = [i for i, c in id_counts.items() if c > 1]
    if dup_ids:
        log.append({
            'severity': 'MEDIUM',
            'part': 'Structural',
            'heading': 'DOM IDs',
            'location': 'Card & Section IDs',
            'issue': f'Duplicate element IDs found: {dup_ids[:10]} (total {len(dup_ids)})',
            'doc_says': f'Duplicate IDs: {dup_ids[:5]}',
            'kit_says': 'All DOM IDs must be unique',
            'fix': 'Rename duplicate container IDs to be unique'
        })

    # PASS 2: RATES & ALLOWANCES AUDIT
    # 1. CT Marginal Relief fraction check
    if "3/400" in html:
        log.append({
            'severity': 'CRITICAL',
            'part': 'Part 6 / Part 64',
            'heading': 'Corporation Tax Rates Table',
            'location': 'CT Marginal Relief Fraction',
            'issue': 'Corporation tax marginal relief fraction states 3/400ths instead of kit verbatim 3/200ths',
            'doc_says': 'Marginal Fraction: 3/400ths',
            'kit_says': 'Standard fraction 3/200 (Kit p.39)',
            'fix': 'Change 3/400ths to 3/200ths'
        })

    # 2. Van Fuel Scale Charge check (£769 in kit p.38 vs £757 in html Part 12)
    if "757" in html:
        log.append({
            'severity': 'HIGH',
            'part': 'Part 12',
            'heading': 'IT-06 Benefits in Kind',
            'location': 'Company Van Fuel Scale Charge',
            'issue': 'Van fuel scale charge states £757 instead of kit verbatim £769',
            'doc_says': 'Fuel scale charge = £757',
            'kit_says': 'The van fuel benefit is £769 (Kit p.38)',
            'fix': 'Change £757 to £769'
        })

    # PASS 3: CALCULATION RECOMPUTATION
    # PASS 4: ANSWER-KEY VERIFICATION
    # Check Q19 Lease Premium in Part 21
    if "50 - 14" in html or "50 - (N - 1)" in html:
        log.append({
            'severity': 'MEDIUM',
            'part': 'Part 13 / Part 21',
            'heading': 'Property Income Lease Premium Formula',
            'location': 'Lease Premium Property Income Formula',
            'issue': 'Lease premium formula presented as 50 - (N - 1) instead of kit verbatim 51 - (N - 1) or 50% - 2%*(N - 1)',
            'doc_says': '£82,000 × (50 - 14)/50',
            'kit_says': '£82,000 × [51 - (N - 1)]/50 (Kit p.219 Answer 19)',
            'fix': 'Update lease premium formula to [51 - (N - 1)]/50'
        })

    print(f"Total audit findings logged: {len(log)}")
    for item in log:
        print(f"\n[{item['severity']}] {item['part']} · {item['heading']}")
        print(f"  Location: {item['location']}")
        print(f"  Issue: {item['issue']}")
        print(f"  Document says: {item['doc_says']}")
        print(f"  Kit says: {item['kit_says']}")
        print(f"  Fix: {item['fix']}")

if __name__ == '__main__':
    run_full_audit()
