import requests
import time
from bs4 import BeautifulSoup
import json
import os

class Companies:
    def __init__(self, company, description):
        self.company = company
        self.description = description

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)


print(os.path.abspath(r"C:\Users\Daniel\Documents\SustainAndGain\presentationFiles"))

companies = []
Description = []


with open('PresentationTickers.txt', 'r') as _:
    for line in _:
        line = line.strip()
        if line:
            companies.append(line)

for value in companies:
    print(value)

for company in companies:
    try:
        website_url = requests.get(f'https://www.di.se/bors/aktier/{company}/').text
        soup = BeautifulSoup(website_url,'lxml')
        My_table = soup.find('div',{'class':'di_stock-company-info__column'}).get_text(strip=True)
        time.sleep(1)
    except:
        continue

    person = Companies(company, My_table)
    s = json.dumps(person.__dict__, ensure_ascii=False)

    Description.append(s)
    print(s)


with open('presentationTickersDone.json', 'w') as f:
    f.write("[")
    for item in Description:
        f.write("%s\n" % item)

    f.write("]")
