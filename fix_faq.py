import re

with open('/Users/cp/Ronak/CP/CP Website/servicepages/industry-template.html', 'r') as f:
    t = f.read()

# Replace the FAQ list
old_faq = re.search(r'<div class="faq-list">.*?</div>\s*</div>\s*</section>', t, re.DOTALL).group(0)

new_faq = """<div class="faq-list">
          <div class="faq-item" data-faq>
            <button class="faq-trigger" aria-expanded="false">
              <div class="faq-trigger-q">Does this support Restricted Use Pesticide (RUP) recordkeeping?</div>
              <div class="faq-trigger-dot"></div>
            </button>
            <div class="faq-answer" role="region">
              <div class="faq-answer-inner">Yes — purchase and application records for RUPs are tied to certified-applicator data at the point of scan, supporting FIFRA's recordkeeping requirements.</div>
            </div>
          </div>

          <div class="faq-item" data-faq>
            <button class="faq-trigger" aria-expanded="false">
              <div class="faq-trigger-q">Can safety and application information reach our applicator network in multiple languages?</div>
              <div class="faq-trigger-dot"></div>
            </button>
            <div class="faq-answer" role="region">
              <div class="faq-answer-inner">Yes — dosage, tank-mix, and safety guidance can be delivered in the applicator's preferred language at the point of scan, supporting WPS accessibility requirements.</div>
            </div>
          </div>

          <div class="faq-item" data-faq>
            <button class="faq-trigger" aria-expanded="false">
              <div class="faq-trigger-q">How does this integrate with our existing distributor and ERP systems?</div>
              <div class="faq-trigger-dot"></div>
            </button>
            <div class="faq-answer" role="region">
              <div class="faq-answer-inner">Smart Epsilon connects to SAP, Oracle, and other major ERPs without rip-and-replace, via GS1 EPCIS 2.0. Most agrochemical clients are live in about six weeks.</div>
            </div>
          </div>

          <div class="faq-item" data-faq>
            <button class="faq-trigger" aria-expanded="false">
              <div class="faq-trigger-q">During a state inspection, can we produce batch-level records on demand?</div>
              <div class="faq-trigger-dot"></div>
            </button>
            <div class="faq-answer" role="region">
              <div class="faq-answer-inner">Yes — batch and dealer-level data is queryable in real time, tied to each product's EPA registration number, for audit-readiness during State Lead Agency inspection.</div>
            </div>
          </div>
        </div>
      </div>
    </section>"""
t = t.replace(old_faq, new_faq)

with open('/Users/cp/Ronak/CP/CP Website/servicepages/industry-template.html', 'w') as f:
    f.write(t)

print("FAQ replaced!")
