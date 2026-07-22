with open('/Users/cp/Ronak/CP/CP Website/servicepages/solution-anti-counterfeiting.html', 'r') as f:
    content = f.read()

# Replace the questions with statements or remove them
content = content.replace(
    '<h3 style="font-size: 1.25rem; font-weight: 800; color: #111111; margin-bottom: 0.5rem;">Can we measure the ROI of this system?</h3>',
    '<h3 style="font-size: 1.25rem; font-weight: 800; color: #111111; margin-bottom: 0.5rem;">Measurable ROI</h3>'
)
content = content.replace(
    '<h3 style="font-size: 1.25rem; font-weight: 800; color: #111111; margin-bottom: 0.5rem;">Will this hold up in a court of law during a dispute?</h3>',
    '<h3 style="font-size: 1.25rem; font-weight: 800; color: #111111; margin-bottom: 0.5rem;">Legally Admissible Proof</h3>'
)
content = content.replace(
    '<h3 style="font-size: 1.25rem; font-weight: 800; color: #111111; margin-bottom: 0.5rem;">Will this slow down our production line?</h3>',
    '<h3 style="font-size: 1.25rem; font-weight: 800; color: #111111; margin-bottom: 0.5rem;">Zero Production Slowdown</h3>'
)
content = content.replace(
    '<h3 style="font-size: 1.25rem; font-weight: 800; color: #111111; margin-bottom: 0.5rem;">Does this affect our packaging design?</h3>',
    '<h3 style="font-size: 1.25rem; font-weight: 800; color: #111111; margin-bottom: 0.5rem;">Preserved Brand Aesthetics</h3>'
)

with open('/Users/cp/Ronak/CP/CP Website/servicepages/solution-anti-counterfeiting.html', 'w') as f:
    f.write(content)

print("Fixed questions.")
