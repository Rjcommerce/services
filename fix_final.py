import re

files = [
    '/Users/cp/Ronak/CP/CP Website/servicepages/solution-anti-counterfeiting.html',
    '/Users/cp/Ronak/CP/CP Website/servicepages/industry-template.html'
]

for file_path in files:
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Fix .vstep-outline-num clipping issue for "02" and "04"
    old_css = """.vstep-outline-num {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 4rem;
  font-weight: 900;
  color: transparent;
  -webkit-text-stroke: 1.5px rgba(0,0,0,0.1);
  line-height: 0.8;
  margin-bottom: 4px;
  margin-left: -2px;
  transition: -webkit-text-stroke 0.4s ease;
}"""
    new_css = """.vstep-outline-num {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 4rem;
  font-weight: 900;
  color: transparent;
  -webkit-text-stroke: 1.5px rgba(0,0,0,0.1);
  line-height: 0.8;
  margin-bottom: 4px;
  margin-left: -2px;
  padding-left: 4px;
  transition: -webkit-text-stroke 0.4s ease;
}"""
    content = content.replace(old_css, new_css)

    # 2. Fix comparison table full row hover
    old_hover = ".comparison-table tbody tr:hover td {"
    if old_hover in content:
        # Just replace the hover block
        # We need to find the block
        content = re.sub(
            r'\.comparison-table tbody tr:hover td \{.*?\}',
            '.comparison-table tbody tr:hover td { background: rgba(104,98,167,0.05); }\n.comparison-table tbody tr:hover td.cell-smart { background: rgba(104,98,167,0.12); }',
            content, flags=re.DOTALL
        )

    with open(file_path, 'w') as f:
        f.write(content)

print("Fixed vstep numbers and table row hover.")
