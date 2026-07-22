import re

with open('build_agrochemicals_from_doc.py', 'r') as f:
    content = f.read()

# Replace the wrong regex with the correct one
content = content.replace(
    r"old_sticky_stack = re.search(r'<div class=\"vstep-stack\">.*?</div>\s*</div>\s*</section>', template, re.DOTALL).group(0)",
    r"old_sticky_stack = re.search(r'<div class=\"vstep-list\">.*?</section>', template, re.DOTALL).group(0)"
)

# Replace the new HTML structure to match vstep-list properly
old_html = """<div class="vstep-stack">
          <!-- Impact 1 -->
          <div class="vstep-card">
            <div class="vstep-outline-num">01</div>
            <div class="vstep-content">
              <h3 class="vstep-title">End-to-End Product Visibility</h3>
              <p class="vstep-desc">From formulation to field, know where every unit is at every stage — not just inside your own four walls.</p>
            </div>
          </div>"""

new_html = """<div class="vstep-list">
          <div class="vstep-progress-line"></div>
          
          <!-- Impact 1 -->
          <div class="vstep-item">
            <div class="vstep-icon"><svg class="icon" width="20" height="20"><use href="#icon-check"/></svg></div>
            <div class="vstep-content">
              <div class="vstep-outline-num">01</div>
              <h3 class="vstep-title">End-to-End Product Visibility</h3>
              <p class="vstep-desc">From formulation to field, know where every unit is at every stage — not just inside your own four walls.</p>
            </div>
          </div>"""
content = content.replace(old_html, new_html)

# Add remaining impacts using the new structure
for i, title, desc in [
    (2, "Protected Brand Trust & Liability", "Fewer efficacy complaints and liability disputes traced back to spurious product. Defensible records of dosage communication reduce misapplication claims."),
    (3, "Accurate Demand Planning", "Production and inventory decisions built on real, verified sell-through — not shipment estimates that turn out wrong by harvest."),
    (4, "Audit-Ready Compliance", "Batch-level FIFRA, RUP, and WPS records available in minutes during a state or federal inspection, not reconstructed under deadline pressure."),
    (5, "Stronger Dealer Relationships", "Faster, dispute-resistant incentive payouts that reward what a dealer actually sold — protecting shelf space at the next reorder.")
]:
    old_card = f"""          <div class="vstep-card">
            <div class="vstep-outline-num">0{i}</div>
            <div class="vstep-content">
              <h3 class="vstep-title">{title}</h3>
              <p class="vstep-desc">{desc}</p>
            </div>
          </div>"""
    new_card = f"""          <div class="vstep-item">
            <div class="vstep-icon"><svg class="icon" width="20" height="20"><use href="#icon-check"/></svg></div>
            <div class="vstep-content">
              <div class="vstep-outline-num">0{i}</div>
              <h3 class="vstep-title">{title}</h3>
              <p class="vstep-desc">{desc}</p>
            </div>
          </div>"""
    content = content.replace(old_card, new_card)

# Close the section properly
content = content.replace(
    """        </div>
      </div>
    </section>""",
    """        </div>
      </div>
    </section>"""
)

with open('build_agrochemicals_from_doc.py', 'w') as f:
    f.write(content)

