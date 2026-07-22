import docx

doc_path = "/Users/cp/Ronak/Smart Epsilon/Antigravity/Smart Epsilon Website Pages Content.docx"
doc = docx.Document(doc_path)

content = []
for p in doc.paragraphs:
    if p.text.strip():
        content.append(p.text.strip())

with open('/Users/cp/.gemini/antigravity/brain/675b45b3-1249-4cd2-a478-97874d96a273/scratch/all_content.txt', 'w') as f:
    f.write('\n'.join(content))
