with open('/Users/cp/.gemini/antigravity/brain/675b45b3-1249-4cd2-a478-97874d96a273/scratch/build_anti_counterfeiting_page.py', 'r') as f:
    content = f.read()

# Fix 1: Arial font for outline numbers to prevent variable font overlapping paths
content = content.replace(
    'font-family: system-ui, -apple-system, sans-serif;',
    'font-family: Arial, Helvetica, sans-serif;'
)

# Fix 2: Override td backgrounds on tr hover
old_hover = ".comparison-table tbody tr:hover {\n  background-color: rgba(104, 98, 167, 0.05);\n}"
new_hover = ".comparison-table tbody tr:hover td {\n  background: rgba(104, 98, 167, 0.08) !important;\n}"
content = content.replace(old_hover, new_hover)

with open('/Users/cp/.gemini/antigravity/brain/675b45b3-1249-4cd2-a478-97874d96a273/scratch/build_anti_counterfeiting_page.py', 'w') as f:
    f.write(content)
