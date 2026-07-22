import re

with open('/Users/cp/Ronak/CP/CP Website/servicepages/solution-anti-counterfeiting.html', 'r') as f:
    template = f.read()

# 1. Page Title & Meta
template = re.sub(
    r'<title>.*?</title>',
    '<title>Agrochemicals Industry | Smart Epsilon</title>',
    template, flags=re.DOTALL
)
template = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Smart Epsilon gives agrochemical manufacturers plant-to-field visibility, verified authenticity, and dealer accountability.">',
    template, flags=re.DOTALL
)

# 2. Hero Section
template = template.replace('Anti-Counterfeiting Solution', 'AGROCHEMICALS')
template = template.replace('Protect revenue and reputation from the factory to the field.', 'Every bag verified. Every dealer accountable. Every acre protected.')
template = template.replace('Deploy multi-layered authentication to detect cloned packaging, eliminate grey market diversion, and secure brand trust at the unit level.', "Smart Epsilon gives agrochemical manufacturers plant-to-field visibility, verified authenticity, and dealer accountability — so spurious product, misapplication liability, and channel disputes get caught before they cost you a season's trust.")

# Pills
template = template.replace('Overt & Covert Protection', 'EPA / FIFRA-ready compliance')
template = template.replace('Geo-Clone Detection', 'Works with your ERP')
template = template.replace('Forensic Watermarking', 'Live in ~6 weeks')

# Right Card (Keep structure, change text)
template = template.replace('How the 3-Layer System Works', 'Real-world impact')
template = template.replace('Level 1: Overt', 'Plant-to-field visibility')
template = template.replace('Visible Nano-Holograms for quick visual verification by channel partners.', 'Track every bag from the moment it leaves the formulation plant to the moment a grower opens it.')
template = template.replace('Level 2: Covert', 'Dealer Accountability')
template = template.replace('Hidden Geo-Clone markers flag unauthorized bulk scans instantly.', 'Automated payouts built on verified sell-through data, not self-reported shipment numbers.')
template = template.replace('Level 3: Forensic', 'Brand Protection')
template = template.replace('Invisible AI watermarks embedded into the packaging print itself.', 'Stop spurious look-alikes from destroying your brand reputation in the field.')

# 3. Vertical Quotes (Real Supply Chain Problems)
old_quotes = re.search(r'<div class="quote-wall-inner">.*?</div>\s*</section>', template, re.DOTALL).group(0)

new_quotes = """<div class="quote-wall-inner">
      <div class="quote-block">
        <div class="quote-number-wrap"><span class="quote-number-large" style="color: #ef4444;">01</span><div class="quote-icon" style="background: rgba(239, 68, 68, 0.1); color: #ef4444;"><svg class="icon" width="24" height="24"><use href="#icon-alert-triangle"/></svg></div></div>
        <div class="quote-content">
          <h3 class="quote-text" style="font-size: 24px;">Spurious Product in the Channel</h3>
          <p class="quote-author" style="margin-top: 12px; font-size: 16px;">"Your biggest ag retailer is quietly stocking a look-alike at 20% below your list price. Can you prove to a grower which bag is real?" Unregistered formulators and repackagers sell copies that look right on the shelf — a grower finds out only when the spray fails.</p>
        </div>
      </div>
      <div class="quote-block">
        <div class="quote-number-wrap"><span class="quote-number-large" style="color: #f59e0b;">02</span><div class="quote-icon" style="background: rgba(245, 158, 11, 0.1); color: #f59e0b;"><svg class="icon" width="24" height="24"><use href="#icon-trend"/></svg></div></div>
        <div class="quote-content">
          <h3 class="quote-text" style="font-size: 24px;">Sell-In Doesn't Equal Sell-Out</h3>
          <p class="quote-author" style="margin-top: 12px; font-size: 16px;">"Distributor orders looked strong all season. Why is next year's demand forecast already wrong?" What shipped and what actually moved through the dealer network to a grower are different numbers — and production plans get built on the wrong one.</p>
        </div>
      </div>
      <div class="quote-block">
        <div class="quote-number-wrap"><span class="quote-number-large" style="color: #3b82f6;">03</span><div class="quote-icon" style="background: rgba(59, 130, 246, 0.1); color: #3b82f6;"><svg class="icon" width="24" height="24"><use href="#icon-report"/></svg></div></div>
        <div class="quote-content">
          <h3 class="quote-text" style="font-size: 24px;">Regulatory Audit, No Notice</h3>
          <p class="quote-author" style="margin-top: 12px; font-size: 16px;">"A State Lead Agency inspector wants batch-level RUP records and WPS documentation — this week." Reconstructing that from spreadsheets turns a routine inspection into a multi-day scramble.</p>
        </div>
      </div>
      <div class="quote-block">
        <div class="quote-number-wrap"><span class="quote-number-large" style="color: #8b5cf6;">04</span><div class="quote-icon" style="background: rgba(139, 92, 246, 0.1); color: #8b5cf6;"><svg class="icon" width="24" height="24"><use href="#icon-shield"/></svg></div></div>
        <div class="quote-content">
          <h3 class="quote-text" style="font-size: 24px;">Misapplication Liability</h3>
          <p class="quote-author" style="margin-top: 12px; font-size: 16px;">"A grower used the wrong dosage, and now there's a crop-failure claim with your name on it." The liability conversation starts with your brand, whether or not the product was ever the actual problem.</p>
        </div>
      </div>
      <div class="quote-block">
        <div class="quote-number-wrap"><span class="quote-number-large" style="color: #10b981;">05</span><div class="quote-icon" style="background: rgba(16, 185, 129, 0.1); color: #10b981;"><svg class="icon" width="24" height="24"><use href="#icon-users"/></svg></div></div>
        <div class="quote-content">
          <h3 class="quote-text" style="font-size: 24px;">Dealer Trust & Channel Loyalty</h3>
          <p class="quote-author" style="margin-top: 12px; font-size: 16px;">"Your dealer's incentive payout has been stuck in review for six weeks. Why would they push your product this season?" Slow, disputed rebate programs cost the shelf space the payout was supposed to buy.</p>
        </div>
      </div>
    </div>
  </section>"""
template = template.replace(old_quotes, new_quotes)
template = template.replace('Agrochemical supply chains break in more ways than any one page can cover — here are the five that cost the most, most often.', 'Agrochemical supply chains break in more ways than any one page can cover — here are the five that cost the most, most often.')

# 4. Solutions Carousel
template = template.replace('What it actually solves', 'Solutions')
template = template.replace("The problems you didn't think could be fixed", 'Ten specific problems Smart Epsilon solves')
template = template.replace('Counterfeiting creates a ripple effect of operational headaches. We address the root cause.', 'Actionable capabilities engineered specifically for agrochemical manufacturers.')

old_slider = re.search(r'<div class="bento-slider">.*?</div>\s*</div>\s*</section>', template, re.DOTALL).group(0)

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
template = template.replace(old_slider, new_slider)


# 5. How Each Solution Applies to Agrochemicals
template = template.replace('Fits the stack you already run', 'How Each Solution Applies')
template = template.replace('No rip-and-replace required.', 'Agrochemical Implementations')
template = template.replace('We built Smart Epsilon to plug into the systems your production lines and warehouses already depend on.', 'Horizontal stacked cards showing agro-specific implementation and business impact.')

old_int_grid = re.search(r'<div class="integration-grid">.*?</div>\s*</div>\s*</section>', template, re.DOTALL).group(0)

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
template = template.replace(old_int_grid, new_int_grid)

# 6. Business Impact (Sticky list section using vstep-list)
template = template.replace('Cross-functional alignment', 'Business Impact')
template = template.replace('One rollout process', 'What this adds up to')
template = template.replace('Enterprise software shouldn\'t mean endless consulting hours. We deploy on a rigid, proven timeline.', 'Across an agrochemical manufacturing operation.')

old_sticky_stack = re.search(r'<div class="vstep-list">.*?</section>', template, re.DOTALL).group(0)

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
template = template.replace(old_sticky_stack, new_sticky_stack)

# 7. Compliance Context
template = template.replace("However you're evaluating this", 'Compliance & Regulatory Context')
template = template.replace('Inside the Platform', 'FIFRA, EPA registration, and state pesticide law')
template = template.replace('Whether you are the Plant Manager, IT Director, or Brand Protection Lead, the system delivers exactly what you need.', 'Handled, not hoped for.')

template = template.replace('Unit-Level Serialisation', 'FIFRA / EPA Registration Alignment')
template = template.replace('Track every single product from the manufacturing line down to the retail shelf with unique 2D codes.', "Serialization ties directly to each product's EPA registration number, the identifier regulators and state inspectors check first.")

template = template.replace('Covert Geo-Tracking', 'Restricted Use Pesticide (RUP) Tracking')
template = template.replace('Invisible markers that trigger alerts when a product is scanned outside its authorized sales territory.', "Purchase and application records tied to certified-applicator data, supporting the recordkeeping FIFRA requires.")

template = template.replace('Predictive Alerts', 'Worker Protection Standard (WPS)')
template = template.replace('AI models automatically highlight suspicious scan patterns before counterfeits hit critical mass in the market.', "Point-of-scan delivery of Restricted Entry Interval (REI), Pre-Harvest Interval (PHI), and safety guidance, in the applicator's preferred language.")

# 8. Testimonials
template = template.replace('Supply Chain VP, Automotive', 'Head of Brand Protection, Agrochemicals major')
template = template.replace('"We used to find out about counterfeit parts when a furious customer brought a failed transmission to a dealership. Smart Epsilon flagged three illicit distributor shipments in our first quarter live. The ROI was instantaneous."', '"Smart Epsilon\'s anti-counterfeiting solution cut counterfeit-driven complaints sharply in our first two quarters. Our field team now spots clones before customers do."')

# 9. Book Demo
template = template.replace('Book a demo', 'See it in action')
template = template.replace('Ready to see', 'Ready to see')
template = template.replace('your chain', 'your chain')
template = template.replace('live?', 'live?')
template = template.replace('Explore the platform with your real business challenges in mind.', 'See how Smart Epsilon protects your formulation, your dealer network, and the growers who trust your label.')

with open('/Users/cp/Ronak/CP/CP Website/servicepages/industry-template.html', 'w') as f:
    f.write(template)

print("Final correct agrochemicals layout pushed!")
