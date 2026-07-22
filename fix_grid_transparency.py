with open('/Users/cp/.gemini/antigravity/brain/675b45b3-1249-4cd2-a478-97874d96a273/scratch/build_anti_counterfeiting_page.py', 'r') as f:
    content = f.read()

# Replace the base fill color of the hero grid boxes
content = content.replace(
    "rect.setAttribute('fill', 'rgba(30, 34, 59, 0.5)');",
    "rect.setAttribute('fill', 'rgba(30, 34, 59, 0.3)');"
)

content = content.replace(
    "this.setAttribute('fill', 'rgba(30, 34, 59, 0.5)');",
    "this.setAttribute('fill', 'rgba(30, 34, 59, 0.3)');"
)

with open('/Users/cp/.gemini/antigravity/brain/675b45b3-1249-4cd2-a478-97874d96a273/scratch/build_anti_counterfeiting_page.py', 'w') as f:
    f.write(content)
