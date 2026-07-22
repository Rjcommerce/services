import re

# Read the newly polished solution template
with open('/Users/cp/Ronak/CP/CP Website/servicepages/solution-anti-counterfeiting.html', 'r') as f:
    template = f.read()

# Start replacing the content with Agrochemicals content

# 1. Update Title and Meta
template = re.sub(
    r'<title>.*?</title>',
    '<title>Agrochemicals & Crop Protection Industry | Smart Epsilon</title>',
    template, flags=re.DOTALL
)
template = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Unit-level supply chain traceability, anti-counterfeiting, and channel intelligence purpose-built for agrochemical manufacturers.">',
    template, flags=re.DOTALL
)

# 2. Hero Section
template = template.replace('Anti-Counterfeiting Solution', 'Agrochemicals & Crop Protection')
template = template.replace('Protect revenue and reputation from the factory to the field.', 'Defend high-value formulations from plant to farm.')
template = template.replace('Deploy multi-layered authentication to detect cloned packaging, eliminate grey market diversion, and secure brand trust at the unit level.', 'Unit-level serialization, 3-layer anti-counterfeiting, and automated channel visibility designed for high-consequence chemical products and complex distributor networks.')

# Hero Trust Chips
template = template.replace('Overt & Covert Protection', 'GS1 EPCIS 2.0 Native')
template = template.replace('Geo-Clone Detection', 'High-Speed Line Activation')
template = template.replace('Forensic Watermarking', 'Zero ERP Overhaul')

# Hero Right Card
template = template.replace('How the 3-Layer System Works', 'Built for Agrochemical Realities')

# Hero Right Card Points
template = template.replace('Level 1: Overt', '3-Layer Protection')
template = template.replace('Visible Nano-Holograms for quick visual verification by channel partners.', 'Overt nano-hologram + Covert geo-clone flags + AI invisible watermark.')

template = template.replace('Level 2: Covert', 'Distributor & Depot Chain of Custody')
template = template.replace('Hidden Geo-Clone markers flag unauthorized bulk scans instantly.', 'Automated case & pallet aggregation across multi-tier channels.')

template = template.replace('Level 3: Forensic', 'Audit-Ready Compliance')
template = template.replace('Invisible AI watermarks embedded into the packaging print itself.', 'Produce complete batch histories for regulators in minutes, not weeks.')


# 3. Vertical Quotes (Sector Challenges)
template = template.replace('Real Supply Chain Problems', 'Sector Challenges')
template = template.replace('The cost of not knowing', 'Why Traditional Traceability Fails')
template = template.replace('Counterfeits and channel leakage don’t just hit revenue—they erode brand equity, create liability, and blind your supply chain.', 'Agrochemical packaging faces extreme environmental conditions, high counterfeit incentives, and multi-layered distribution tiers.')

old_vertical_quotes_section = re.search(r'<div class="quote-wall-inner">.*?</div>\s*</section>', template, re.DOTALL).group(0)

new_vertical_quotes = """<div class="quote-wall-inner">
      
      <!-- Quote 1 -->
      <div class="quote-block">
        <div class="quote-number-wrap">
          <span class="quote-number-large" style="color: #ef4444;">01</span>
          <div class="quote-icon" style="background: rgba(239, 68, 68, 0.1); color: #ef4444;">
            <svg class="icon" width="24" height="24"><use href="#icon-barcode"/></svg>
          </div>
        </div>
        <div class="quote-content">
          <h3 class="quote-text" style="font-size: 24px;">Easily Copied 1D/2D Barcodes</h3>
          <p class="quote-author" style="margin-top: 12px; font-size: 16px;">Standard QR codes can be photographed and printed onto fake formulations in bulk. Without covert geo-clone tracking, fakes go undetected until crop failure occurs.</p>
        </div>
      </div>

      <!-- Quote 2 -->
      <div class="quote-block">
        <div class="quote-number-wrap">
          <span class="quote-number-large" style="color: #f59e0b;">02</span>
          <div class="quote-icon" style="background: rgba(245, 158, 11, 0.1); color: #f59e0b;">
            <svg class="icon" width="24" height="24"><use href="#icon-truck"/></svg>
          </div>
        </div>
        <div class="quote-content">
          <h3 class="quote-text" style="font-size: 24px;">Distributor Channel Diversion</h3>
          <p class="quote-author" style="margin-top: 12px; font-size: 16px;">Subsidized chemical products intended for one state are quietly diverted to secondary markets. Without automated receipt confirmation, you lose channel discipline.</p>
        </div>
      </div>

      <!-- Quote 3 -->
      <div class="quote-block">
        <div class="quote-number-wrap">
          <span class="quote-number-large" style="color: #3b82f6;">03</span>
          <div class="quote-icon" style="background: rgba(59, 130, 246, 0.1); color: #3b82f6;">
            <svg class="icon" width="24" height="24"><use href="#icon-alert"/></svg>
          </div>
        </div>
        <div class="quote-content">
          <h3 class="quote-text" style="font-size: 24px;">Slow Regulatory Audits</h3>
          <p class="quote-author" style="margin-top: 12px; font-size: 16px;">Reconstructing a chemical lot's journey across disparate software systems pulls IT, legal, and plant managers into multi-week war rooms during inspections.</p>
        </div>
      </div>

      <!-- Quote 4 -->
      <div class="quote-block">
        <div class="quote-number-wrap">
          <span class="quote-number-large" style="color: #8b5cf6;">04</span>
          <div class="quote-icon" style="background: rgba(139, 92, 246, 0.1); color: #8b5cf6;">
            <svg class="icon" width="24" height="24"><use href="#icon-lock"/></svg>
          </div>
        </div>
        <div class="quote-content">
          <h3 class="quote-text" style="font-size: 24px;">Heavy Retraining Overhead</h3>
          <p class="quote-author" style="margin-top: 12px; font-size: 16px;">Complex WMS add-ons require months of staff retraining. Smart Epsilon equips plant floor operators with intuitive mobile workflows trained in under a week.</p>
        </div>
      </div>

    </div>
  </section>"""
template = template.replace(old_vertical_quotes_section, new_vertical_quotes)


# 4. Bento Slider Carousel (Plant-to-Farm Chain of Custody)
template = template.replace('What it actually solves', 'End-to-End Pipeline')
template = template.replace("The problems you didn't think could be fixed", 'Plant-to-Farm Chain of Custody')
template = template.replace('Counterfeiting creates a ripple effect of operational headaches. We address the root cause.', 'A single continuous record of identity, ownership, and scan location from chemical synthesis to retail purchase.')

slider_match = re.search(r'<div class="bento-slider">.*?</div>\s*</div>\s*</section>', template, re.DOTALL)
if slider_match:
    old_slider = slider_match.group(0)
    new_slider = """<div class="bento-slider">
          <div class="bento-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <div class="bento-icon" style="color: #6862a7; background: rgba(104, 98, 167, 0.1);"><svg class="icon" width="24" height="24"><use href="#icon-box"/></svg></div>
            <h3 class="bento-title">Plant Printing</h3>
            <p class="bento-desc">High-speed serialization & nano-OVD label application at 600 BPM.</p>
            <div class="bento-impact"><svg class="icon" width="16" height="16"><use href="#icon-check"/></svg> 01</div>
          </div>

          <div class="bento-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <div class="bento-icon" style="color: #3b82f6; background: rgba(59, 130, 246, 0.1);"><svg class="icon" width="24" height="24"><use href="#icon-trend"/></svg></div>
            <h3 class="bento-title">Aggregation</h3>
            <p class="bento-desc">Parent-child bundle, case, and pallet pairing with GS1 EPCIS standards.</p>
            <div class="bento-impact"><svg class="icon" width="16" height="16"><use href="#icon-check"/></svg> 02</div>
          </div>

          <div class="bento-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <div class="bento-icon" style="color: #10b981; background: rgba(16, 185, 129, 0.1);"><svg class="icon" width="24" height="24"><use href="#icon-route"/></svg></div>
            <h3 class="bento-title">Depot Transfer</h3>
            <p class="bento-desc">Mobile dispatch verification at central distribution hubs.</p>
            <div class="bento-impact"><svg class="icon" width="16" height="16"><use href="#icon-check"/></svg> 03</div>
          </div>

          <div class="bento-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <div class="bento-icon" style="color: #f59e0b; background: rgba(245, 158, 11, 0.1);"><svg class="icon" width="24" height="24"><use href="#icon-truck"/></svg></div>
            <h3 class="bento-title">Retailer Receipt</h3>
            <p class="bento-desc">Geo-tagged check-in confirming authorized regional inventory.</p>
            <div class="bento-impact"><svg class="icon" width="16" height="16"><use href="#icon-check"/></svg> 04</div>
          </div>

          <div class="bento-card" data-tilt data-tilt-max="3" data-tilt-speed="400" data-tilt-glare data-tilt-max-glare="0.05">
            <div class="bento-icon" style="color: #ef4444; background: rgba(239, 68, 68, 0.1);"><svg class="icon" width="24" height="24"><use href="#icon-shield"/></svg></div>
            <h3 class="bento-title">Farm Validation</h3>
            <p class="bento-desc">Instant consumer naked-eye check and mobile scan confirmation.</p>
            <div class="bento-impact"><svg class="icon" width="16" height="16"><use href="#icon-check"/></svg> 05</div>
          </div>
        </div>
      </div>
    </section>"""
    template = template.replace(old_slider, new_slider)


# 5. Grid Cards (Risk Mitigation - 3 columns)
template = template.replace('Fits the stack you already run', 'Risk Mitigation')
template = template.replace('No rip-and-replace required.', 'Automated Channel Leakage Prevention')
template = template.replace('We built Smart Epsilon to plug into the systems your production lines and warehouses already depend on.', 'Protect your brand from unauthorized diversion and tax evasion.')

# Integration 1 -> Risk 1
template = template.replace('ERP &amp; Core Systems', 'Subsidized Stock Diversion')
template = template.replace('Native APIs pull product master data directly from SAP, Oracle, Microsoft Dynamics, or your custom ERP. Batch numbers and SKUs sync automatically.', 'Stops subsidized agricultural products from being quietly resold into non-subsidized commercial markets.')

# Integration 2 -> Risk 2
template = template.replace('Warehouse Hardware', 'Cross-Border Tax Evasion')
template = template.replace('Integrates with Zebra, Honeywell, and Datalogic scanners. Your forklift operators and line workers use the exact same scanners they used yesterday.', 'Automated geofencing flags products scanned in neighboring tax territories without proper customs dispatch.')

# Integration 3 -> Risk 3
template = template.replace('Print &amp; Packaging', 'Expired Lot Distribution')
template = template.replace('Compatible with Domino, Videojet, Markem-Imaje, and industrial continuous inkjet printers. We send the serialized codes, your line prints them at full speed.', 'Prevents expired chemical batches from being re-labeled and sold to unsuspecting farmers in remote regions.')

# Replace Tags on Cards
template = template.replace('>Data Layer<', '>PREVENTED<')
template = template.replace('>Operations Layer<', '>FLAGGED<')
template = template.replace('>Production Layer<', '>BLOCKED<')

# 6. Sticky Stack Cards (Agrochemical Packaging Security Suite)
template = template.replace('Cross-functional alignment', 'Tailored Security')
template = template.replace('One rollout process', 'Agrochemical Packaging Security Suite')
template = template.replace('Zero departmental friction', 'Form-factor specific security')

# Layer 1
template = template.replace('Label Integration', 'Liquid Bottling Lines')
template = template.replace('Packaging teams don’t need to change vendors.', 'Tamper-evident nano-OVD holographic cap seals for high-consequence liquid pesticides.')
template = template.replace('Works seamlessly with your existing print hardware and label suppliers. No capital expenditure required.', 'High-speed inline application preventing illegal refills and brand degradation.')

# Layer 2
template = template.replace('Line Implementation', 'Bulk Chemical Drums')
template = template.replace('Factory floor speed stays exactly the same.', 'Heavy-duty weatherproof barcode labels with GPS depot check-in for 200L industrial drums.')
template = template.replace('Smart Epsilon activates at 600+ BPM. Operators use intuitive scanners with zero complex retraining.', 'Track location and chain of custody seamlessly across borders and harsh environmental conditions.')

# Layer 3
template = template.replace('Field Operations', 'Seed Treatment Packets')
template = template.replace('Sales reps get intelligence, not busywork.', 'Micro-pattern digital watermarks embedded into flexible film packaging during print run.')
template = template.replace('Distributors scan cases via standard mobile apps. Geolocation and timestamp data syncs quietly in the background.', 'Guarantees germination rates by verifying the exact origin and treatment batch before planting.')

# 7. Regulatory Context
template = template.replace("Regulatory Context", "Regulatory Context") # Just in case it wasn't replaced earlier
template = template.replace("However you're evaluating this", 'Regulatory Context')

template = template.replace('Inside the Platform', 'Compliance Capabilities')
template = template.replace('Whether you are the Plant Manager, IT Director, or Brand Protection Lead, the system delivers exactly what you need.', 'Designed specifically to meet stringent agrochemical and pesticide tracking regulations globally.')

template = template.replace('Unit-Level Serialisation', 'FIFRA & EPA Compliance')
template = template.replace('Track every single product from the manufacturing line down to the retail shelf with unique 2D codes.', 'Maintain detailed batch records and supply chain custody data required by agricultural regulatory bodies.')

template = template.replace('Covert Geo-Tracking', 'Cross-State Transport')
template = template.replace('Invisible markers that trigger alerts when a product is scanned outside its authorized sales territory.', 'Automate tax and territory compliance when shipping subsidized fertilizers across state lines.')

template = template.replace('Predictive Alerts', 'Recall Readiness')
template = template.replace('AI models automatically highlight suspicious scan patterns before counterfeits hit critical mass in the market.', 'Execute targeted micro-recalls of specific adulterated batches without pulling unaffected inventory from shelves.')


with open('/Users/cp/Ronak/CP/CP Website/servicepages/industry-template.html', 'w') as f:
    f.write(template)

print("Redesign applied to industry-template.html successfully!")
