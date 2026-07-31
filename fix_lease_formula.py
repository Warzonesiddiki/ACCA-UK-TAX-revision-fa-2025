with open('TX-UK_Revision_Pack.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace any remaining (50 - 14)/50 or (50 - 14)
text = text.replace('(50 - 14)', '(51 - 15)')
text = text.replace('[50 - 14]', '[51 - 15]')
text = text.replace('50 - 14', '51 - 15')
text = text.replace('50 - (15 - 1)', '51 - 15')

with open('TX-UK_Revision_Pack.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated lease formula text.")
