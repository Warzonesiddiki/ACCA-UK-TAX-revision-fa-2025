import re, sys
import pypdf

def apply_patches():
    print("Reading TX-UK_Revision_Pack.html...")
    with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # PATCH 1: CT Marginal Relief Fraction (3/400 -> 3/200)
    html_p1 = html.replace('Marginal Fraction: 3/400ths', 'Marginal Fraction: 3/200ths')
    html_p1 = html_p1.replace('3 / 400', '3 / 200').replace('3/400', '3/200')

    # PATCH 2: Van Fuel Scale Charge (£757 -> £769)
    html_p2 = html_p1.replace('Fuel scale charge = £757', 'Fuel scale charge = £769')
    html_p2 = html_p2.replace('£757', '£769')

    # PATCH 3: Lease Premium Formula ([50 - (N - 1)] -> [51 - (N - 1)])
    html_p3 = html_p2.replace('[50 - (N - 1)]', '[51 - (N - 1)]')
    html_p3 = html_p3.replace('50 - (N - 1)', '51 - (N - 1)')
    html_p3 = html_p3.replace('(50 - 14)', '(51 - 15)')

    # PATCH 4: Deduplicate DOM Element IDs
    # Find all id="..." and make sure card container IDs and drill IDs do not clash
    # Replace id="q1" in drill-card or card with id="drill-q1" or id="card-q1"
    def dedupe_ids(match):
        attr_name = match.group(1)
        val = match.group(2)
        return f'{attr_name}="{val}"'

    # Let's deduplicate IDs by walking through all id="..." tags in order
    seen_ids = set()

    def replace_id(m):
        quote = m.group(1)
        id_val = m.group(2)
        if id_val in seen_ids:
            new_id = f"{id_val}-sec" if not id_val.endswith("-sec") else f"{id_val}-dup"
            seen_ids.add(new_id)
            return f'id={quote}{new_id}{quote}'
        else:
            seen_ids.add(id_val)
            return f'id={quote}{id_val}{quote}'

    html_p4 = re.sub(r'id=(["\'])([^"\']+)\1', replace_id, html_p3)

    with open('TX-UK_Revision_Pack.html', 'w', encoding='utf-8') as f:
        f.write(html_p4)

    print("Patches applied successfully. Re-running audit...")

if __name__ == '__main__':
    apply_patches()
