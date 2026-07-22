from bs4 import BeautifulSoup

with open('/Users/cp/Ronak/CP/CP Website/servicepages/industry-template.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

sections = soup.find_all('section')
for i, sec in enumerate(sections):
    print(f"\n--- SECTION {i+1} ---")
    print(sec.get_text(separator=' | ', strip=True)[:1000])
