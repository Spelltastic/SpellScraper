import urllib.request 
import requests
import bs4
from bs4 import BeautifulSoup
from lxml import html
import yaml
from tqdm import tqdm

URL = "https://www.d20pfsrd.com/magic/all-spells/"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'lxml')
list = soup.find(id='article-content').find_next('div',class_="flexbox")

lis = list.find_all('li')

###################
### METHODS
###################
def getStringSiblings(array, content, stop):
    if content:
        for sibling in content.next_siblings:
            if sibling.name == stop:
                break
            if sibling.name == 'a':
                array.append(sibling.text)
            elif isinstance((sibling), bs4.element.NavigableString):
                component_text = sibling.string.strip()
                if component_text:
                    array.append(component_text.rstrip(';'))
    else:
        return None
    return ' '.join(array)

spellz = {}
pbar = tqdm(total=2650, desc="[Processing]", unit=" spell")

for li in lis:
    url = li.a['href']

    ## get html of details page
    responseDetails = requests.get(url)
    spellSoup = BeautifulSoup(responseDetails.content, 'lxml')

    # get article content which contains all info about spells
    spellContent = spellSoup.find(id='article-content')
    pbar.update(1)

    # get name
    if spellContent :
        spell_name = spellContent.find('h1').text
    else :
        spell_name = None
        continue
    # print("name: ",spell_name)

    # get school and level
    school_levels = spellContent.find('b',string="School").find_previous('p')
    text = school_levels.text
    parts = text.split("Level")
    spell_school = parts[0].replace("School","").strip().strip(";")
    spell_level = parts[1].replace("Level","").strip().split(";")[0]

    spellz[spell_name] = {
        'school': spell_school,
        'level': spell_level,
    }

with open('outputs/spells.yaml', 'w') as f:
    yaml.dump(outputs/levelz, f)

pbar.close()

    

   




