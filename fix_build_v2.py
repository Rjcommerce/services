import re

with open('/Users/cp/Ronak/CP/CP Website/servicepages/solution-anti-counterfeiting.html', 'r') as f:
    t = f.read()

# 1. Hero
t = t.replace('Anti-Counterfeiting Solution', 'AGROCHEMICALS', 1)
t = t.replace('Give counterfeiters three problems, not one.', 'Every bag verified. Every dealer accountable. Every acre protected.')
t = t.replace("Smart Epsilon protects every unit with overt, covert, and forensic verification working together — so a fake doesn't just need to look right, it needs to beat three independent layers at once.", "Smart Epsilon gives agrochemical manufacturers plant-to-field visibility, verified authenticity, and dealer accountability — so spurious product, misapplication liability, and channel disputes get caught before they cost you a season's trust.")

# Pills
t = t.replace('Verified in seconds', 'EPA / FIFRA-ready compliance')
t = t.replace('No device required for first check', 'Works with your ERP')

# Right Card in Hero
t = t.replace('How the 3-Layer System Works', 'Real-world impact')
t = t.replace('Level 1: Overt', 'Plant-to-field visibility')
t = t.replace('Visible Nano-Holograms for quick visual verification by channel partners.', 'Track every bag from the moment it leaves the formulation plant to the moment a grower opens it.')
t = t.replace('Level 2: Covert', 'Dealer Accountability')
t = t.replace('Hidden Geo-Clone markers flag unauthorized bulk scans instantly.', 'Automated payouts built on verified sell-through data, not self-reported shipment numbers.')
t = t.replace('Level 3: Forensic', 'Brand Protection')
t = t.replace('Invisible AI watermarks embedded into the packaging print itself.', 'Stop spurious look-alikes from destroying your brand reputation in the field.')

# 2. Vertical Quotes (Real Supply Chain Problems)
old_quotes = re.search(r'<div class="quote-wall-inner">.*?</div>\s*</section>', t, re.DOTALL).group(0)

new_quotes = """<div class="quote-wall-inner">
      <div class="quote-block">
        <div class="quote-number-wrap"><span class="quote-number-large" style="color: #ef4444;">01</span><div class="quote-icon" style="background: rgba(239, 68, 68, 0.1); color: #ef4444;"><svg class="icon" width="24" height="24"><use href="#icon-alert-triangle"/></svg></div></div>
        <div class="quote-content">
          <h3 class="quote-text" style="font-size: 24px;">Spurious Product in the Channel</h3>
          <p class="quote-author" style="margin-top: 12px; font-size: 16px;">Your biggest ag retailer is quietly stocking a look-alike at 20% below your list price. Can you prove to a grower which bag is real? Unregistered formulators and repackagers sell copies that look right on the shelf — a grower finds out only when the spray fails.</p>
        </div>
      </div>
      <div class="quote-block">
        <div class="quote-number-wrap"><span class="quote-number-large" style="color: #f59e0b;">02</span><div class="quote-icon" style="background: rgba(245, 158, 11, 0.1); color: #f59e0b;"><svg class="icon" width="24" height="24"><use href="#icon-trend"/></svg></div></div>
        <div class="quote-content">
          <h3 class="quote-text" style="font-size: 24px;">Sell-In Doesn't Equal Sell-Out</h3>
          <p class="quote-author" style="margin-top: 12px; font-size: 16px;">Distributor orders looked strong all season. Why is next year's demand forecast already wrong? What shipped and what actually moved through the dealer network to a grower are different numbers — and production plans get built on the wrong one.</p>
        </div>
      </div>
      <div class="quote-block">
        <div class="quote-number-wrap"><span class="quote-number-large" style="color: #3b82f6;">03</span><div class="quote-icon" style="background: rgba(59, 130, 246, 0.1); color: #3b82f6;"><svg class="icon" width="24" height="24"><use href="#icon-report"/></svg></div></div>
        <div class="quote-content">
          <h3 class="quote-text" style="font-size: 24px;">Regulatory Audit, No Notice</h3>
          <p class="quote-author" style="margin-top: 12px; font-size: 16px;">A State Lead Agency inspector wants batch-level RUP records and WPS documentation — this week. Reconstructing that from spreadsheets turns a routine inspection into a multi-day scramble.</p>
        </div>
      </div>
      <div class="quote-block">
        <div class="quote-number-wrap"><span class="quote-number-large" style="color: #8b5cf6;">04</span><div class="quote-icon" style="background: rgba(139, 92, 246, 0.1); color: #8b5cf6;"><svg class="icon" width="24" height="24"><use href="#icon-shield"/></svg></div></div>
        <div class="quote-content">
          <h3 class="quote-text" style="font-size: 24px;">Misapplication Liability</h3>
          <p class="quote-author" style="margin-top: 12px; font-size: 16px;">A grower used the wrong dosage, and now there's a crop-failure claim with your name on it. The liability conversation starts with your brand, whether or not the product was ever the actual problem.</p>
        </div>
      </div>
      <div class="quote-block">
        <div class="quote-number-wrap"><span class="quote-number-large" style="color: #10b981;">05</span><div class="quote-icon" style="background: rgba(16, 185, 129, 0.1); color: #10b981;"><svg class="icon" width="24" height="24"><use href="#icon-users"/></svg></div></div>
        <div class="quote-content">
          <h3 class="quote-text" style="font-size: 24px;">Dealer Trust & Channel Loyalty</h3>
          <p class="quote-author" style="margin-top: 12px; font-size: 16px;">Your dealer's incentive payout has been stuck in review for six weeks. Why would they push your product this season? Slow, disputed rebate programs cost the shelf space the payout was supposed to buy.</p>
        </div>
      </div>
    </div>
  </section>"""
t = t.replace(old_quotes, new_quotes)
t = t.replace('Counterfeiting creates a ripple effect of operational headaches. We address the root cause.', 'Agrochemical supply chains break in more ways than any one page can cover — here are the five that cost the most, most often.')

# 3. Solutions Carousel
t = t.replace('What it actually solves', 'Solutions')
t = t.replace("The problems you didn't think could be fixed.", 'Ten specific problems Smart Epsilon solves for agrochemical manufacturers.')

old_slider = re.search(r'<div class="bento-slider">.*?</div>\s*</div>\s*</section>', t, re.DOTALL).group(0)

new_slider = """<div class="bento-slider">
          <div class="bento-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <h3 class="bento-title">Authenticity Check</h3>
            <p class="bento-desc">Verify a crop protection product's authenticity before purchase — no device required for the first check.</p>
          </div>
          <div class="bento-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <h3 class="bento-title">Real Demand Data</h3>
            <p class="bento-desc">Replace shipment-based demand estimates with real, scan-confirmed sell-through data.</p>
          </div>
          <div class="bento-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <h3 class="bento-title">Audit-Ready</h3>
            <p class="bento-desc">Produce audit-ready batch records for a state or federal inspection in minutes, not days.</p>
          </div>
          <div class="bento-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <h3 class="bento-title">Safety Guidance</h3>
            <p class="bento-desc">Deliver dosage, tank-mix compatibility, and safety guidance at the point of scan, in the applicator's language.</p>
          </div>
          <div class="bento-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <h3 class="bento-title">Automatic Payouts</h3>
            <p class="bento-desc">Calculate dealer incentive payouts automatically from verified sales — not self-reported invoice volume.</p>
          </div>
          <div class="bento-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <h3 class="bento-title">Detect Diversion</h3>
            <p class="bento-desc">Detect counterfeit or diverted product entering regional distribution before it reaches a shelf.</p>
          </div>
          <div class="bento-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <h3 class="bento-title">Loading Accuracy</h3>
            <p class="bento-desc">Confirm loading and unloading accuracy at regional distribution centers in real time.</p>
          </div>
          <div class="bento-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <h3 class="bento-title">Cold-Chain</h3>
            <p class="bento-desc">Monitor temperature compliance for cold-sensitive seed treatments in storage and transit.</p>
          </div>
          <div class="bento-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <h3 class="bento-title">Theft Flagging</h3>
            <p class="bento-desc">Flag shrinkage or theft of high-value patented formulations as it happens, not at the next count.</p>
          </div>
          <div class="bento-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <h3 class="bento-title">Dealer Visibility</h3>
            <p class="bento-desc">Give every dealer real-time visibility into exactly what they've earned, and why.</p>
          </div>
        </div>
      </div>
    </section>"""
t = t.replace(old_slider, new_slider)


# 4. How Each Solution Applies to Agrochemicals
t = t.replace('Fits the stack you already run', 'How Each Solution Applies')
t = t.replace('No rip-and-replace required.', 'Agrochemical Implementations')
t = t.replace('We built Smart Epsilon to plug into the systems your production lines and warehouses already depend on.', 'Horizontal stacked cards showing agro-specific implementation and business impact.')

old_int_grid = re.search(r'<div class="integration-grid">.*?</div>\s*</div>\s*</section>', t, re.DOTALL).group(0)

new_int_grid = """<div class="integration-grid" style="grid-template-columns: repeat(2, 1fr);">
          <div class="int-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <div class="int-card-body">
              <h3 class="int-card-title">1. Track & Trace</h3>
              <p class="int-card-desc"><strong>Implementation:</strong><br/>- Serialization at formulation, tied to EPA registration number.<br/>- Dispatch and receipt confirmed at every regional distribution center.<br/>- Real, scan-verified sell-through data from the dealer network.</p>
              <p class="int-card-desc" style="margin-top: 10px;"><strong>Impact:</strong><br/>- Demand forecasts built on actual sales.<br/>- Audit-ready compliance records in minutes.</p>
            </div>
          </div>
          <div class="int-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <div class="int-card-body">
              <h3 class="int-card-title">2. Anti-Counterfeiting</h3>
              <p class="int-card-desc"><strong>Implementation:</strong><br/>- Tamper-evident holographic label verified in seconds.<br/>- Geo-tagged clone detection flags duplicates.<br/>- Dosage, tank-mix compatibility delivered at point of scan.</p>
              <p class="int-card-desc" style="margin-top: 10px;"><strong>Impact:</strong><br/>- Fewer efficacy complaints traced to spurious product.<br/>- Fewer misapplication liability claims.</p>
            </div>
          </div>
          <div class="int-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <div class="int-card-body">
              <h3 class="int-card-title">3. AI Video Intelligence</h3>
              <p class="int-card-desc"><strong>Implementation:</strong><br/>- Loading/unloading verification at regional centers.<br/>- Thermal monitoring for temperature-sensitive seed treatments.<br/>- Targeted coverage on high-value formulations.</p>
              <p class="int-card-desc" style="margin-top: 10px;"><strong>Impact:</strong><br/>- Freight disputes resolved with visual proof.<br/>- Temperature excursions caught before batch is lost.</p>
            </div>
          </div>
          <div class="int-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <div class="int-card-body">
              <h3 class="int-card-title">4. Payment Linked Incentives</h3>
              <p class="int-card-desc"><strong>Implementation:</strong><br/>- Dealer payouts calculated automatically from verified sell-through.<br/>- Real-time dashboard shows dealers exactly what they earned.</p>
              <p class="int-card-desc" style="margin-top: 10px;"><strong>Impact:</strong><br/>- Faster, dispute-resistant payouts.<br/>- Protected shelf space and loyalty at the next reorder.</p>
            </div>
          </div>
        </div>
      </div>
    </section>"""
t = t.replace(old_int_grid, new_int_grid)

# 5. Business Impact (Sticky list section using vstep-list)
t = t.replace('One rollout process', 'Business Impact')
t = t.replace('Live in ~6 weeks, not 6 months.', 'What this adds up to across an agrochemical manufacturing operation.')
t = t.replace("Enterprise software shouldn't mean endless consulting hours. We deploy on a rigid, proven timeline.", '')

old_sticky_stack = re.search(r'<div class="vstep-list">.*?</section>', t, re.DOTALL).group(0)

new_sticky_stack = """<div class="vstep-list">
          <div class="vstep-progress-line"></div>
          
          <!-- Impact 1 -->
          <div class="vstep-item">
            <div class="vstep-icon"><svg class="icon" width="20" height="20"><use href="#icon-check"/></svg></div>
            <div class="vstep-content">
              <div class="vstep-outline-num">01</div>
              <h3 class="vstep-title">End-to-End Product Visibility</h3>
              <p class="vstep-desc">From formulation to field, know where every unit is at every stage — not just inside your own four walls.</p>
            </div>
          </div>
          <!-- Impact 2 -->
          <div class="vstep-item">
            <div class="vstep-icon"><svg class="icon" width="20" height="20"><use href="#icon-check"/></svg></div>
            <div class="vstep-content">
              <div class="vstep-outline-num">02</div>
              <h3 class="vstep-title">Protected Brand Trust & Liability</h3>
              <p class="vstep-desc">Fewer efficacy complaints and liability disputes traced back to spurious product. Defensible records of dosage communication reduce misapplication claims.</p>
            </div>
          </div>
          <!-- Impact 3 -->
          <div class="vstep-item">
            <div class="vstep-icon"><svg class="icon" width="20" height="20"><use href="#icon-check"/></svg></div>
            <div class="vstep-content">
              <div class="vstep-outline-num">03</div>
              <h3 class="vstep-title">Accurate Demand Planning</h3>
              <p class="vstep-desc">Production and inventory decisions built on real, verified sell-through — not shipment estimates that turn out wrong by harvest.</p>
            </div>
          </div>
          <!-- Impact 4 -->
          <div class="vstep-item">
            <div class="vstep-icon"><svg class="icon" width="20" height="20"><use href="#icon-check"/></svg></div>
            <div class="vstep-content">
              <div class="vstep-outline-num">04</div>
              <h3 class="vstep-title">Audit-Ready Compliance</h3>
              <p class="vstep-desc">Batch-level FIFRA, RUP, and WPS records available in minutes during a state or federal inspection, not reconstructed under deadline pressure.</p>
            </div>
          </div>
          <!-- Impact 5 -->
          <div class="vstep-item">
            <div class="vstep-icon"><svg class="icon" width="20" height="20"><use href="#icon-check"/></svg></div>
            <div class="vstep-content">
              <div class="vstep-outline-num">05</div>
              <h3 class="vstep-title">Stronger Dealer Relationships</h3>
              <p class="vstep-desc">Faster, dispute-resistant incentive payouts that reward what a dealer actually sold — protecting shelf space at the next reorder.</p>
            </div>
          </div>
        </div>
      </div>
    </section>"""
t = t.replace(old_sticky_stack, new_sticky_stack)

# 6. Compliance Context (Replaces features-capsule-tablist section)
t = t.replace("However you're evaluating this", 'Compliance & Regulatory Context')
t = t.replace('Cross-functional alignment.', 'FIFRA, EPA registration, and state pesticide law')
t = t.replace('Different stakeholders have different definitions of success. Smart Epsilon addresses them all.', 'handled, not hoped for.')

# Replace the specific tab titles and contents
t = t.replace('CFO &amp; Finance', 'FIFRA / EPA Registration')
t = t.replace('Legal', 'RUP Tracking')
t = t.replace('Operations', 'WPS Support')
t = t.replace('Marketing', 'State Lead Agency')

# Replace the contents for the 4 tabs
t = t.replace('Measurable ROI', 'FIFRA / EPA Registration Alignment')
t = t.replace('By rejecting unjustified warranty claims, uncovering grey-market diversion, and reclaiming retail space from counterfeits, the system pays for itself in hard ROI within the first year.', "Serialization ties directly to each product's EPA registration number, the identifier regulators and state inspectors check first.")

t = t.replace('Legally Admissible Proof', 'Restricted Use Pesticide (RUP) tracking')
t = t.replace('Yes. The forensic AI watermark creates a non-repudiable audit trail. Our authentication logs provide legally admissible proof of product origin and authenticity.', "Purchase and application records tied to certified-applicator data, supporting the recordkeeping FIFRA requires.")

t = t.replace('Zero Production Slowdown', 'Worker Protection Standard (WPS) support')
t = t.replace('No. Our system integrates directly with standard continuous inkjet printers and warehouse hardware running at full line speed. No custom machinery is required.', "Point-of-scan delivery of Restricted Entry Interval (REI), Pre-Harvest Interval (PHI), and safety guidance, in the applicator's preferred language.")

t = t.replace('Preserved Brand Aesthetics', 'State Lead Agency compliance')
t = t.replace('The Nano-OVD label can be customized to match brand aesthetics, and the forensic AI watermark is invisible to the naked eye. Your packaging looks exactly as intended.', "Every state enforces pesticide law through its own Department of Agriculture, coordinated nationally via AAPCO; batch and dealer-level data support audit-readiness during inspection.")

# 7. Proof / Testimonial
t = t.replace('Supply Chain VP, Automotive', 'Head of Brand Protection, Agrochemicals major')
t = t.replace('"We used to find out about counterfeit parts when a furious customer brought a failed transmission to a dealership. Smart Epsilon flagged three illicit distributor shipments in our first quarter live. The ROI was instantaneous."', '"Smart Epsilon\'s anti-counterfeiting solution cut counterfeit-driven complaints sharply in our first two quarters. Our field team now spots clones before customers do."')
t = t.replace('Global Automotive OEM', "World's largest agrochemical company")
t = t.replace('End-to-end traceability across 15+ countries with unit-level serialization at automotive scale.', "End-to-end visibility across 10+ countries with unit-level serialization at scale.")

# 8. CTA
t = t.replace('Ready to see your chain live?', 'See how Smart Epsilon protects your formulation, your dealer network, and the growers who trust your label.')
t = t.replace('Explore the platform with your real business challenges in mind.', '')
t = t.replace('Book a demo', 'Schedule an Agrochemicals Demo')

with open('/Users/cp/Ronak/CP/CP Website/servicepages/industry-template.html', 'w') as f:
    f.write(t)

print("Final correct agrochemicals layout pushed!")
