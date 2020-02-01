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
    
#fill in your own info
print(os.path.abspath(r".."))

companies = []
Description = []

#fill in your own info
with open('...txt', 'r') as _:
    for line in _:
        line = line.strip()
        if line:
            companies.append(line)

for value in companies:
    print(value)

for company in companies:
    try:                    #fill in your own info
        website_url = requests.get(f'url..').text
        soup = BeautifulSoup(website_url,'lxml')
                            #fill in your own info
        My_table = soup.find('div',{'class':'..htmltag'}).get_text(strip=True)
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
