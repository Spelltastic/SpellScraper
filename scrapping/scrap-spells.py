import urllib.request 
import requests
import bs4
from bs4 import BeautifulSoup
from lxml import html
import yaml
from tqdm import tqdm

### -------------------------------------
# GET ALL THE SPELLS FROM THE PAGE
### -------------------------------------

## GET <li> ELEMENTS NAME + URL TO DETAIL PAGE
# set url for page with all spells
URL = "https://www.d20pfsrd.com/magic/all-spells/"

# get the page content 
response = requests.get(URL)

# parse html using beautifulSoup
soup = BeautifulSoup(response.content, 'lxml')
list = soup.find(id='article-content').find_next('div',class_="flexbox")

# this gets all the <li> elements from the article-content div, which contains all of the 
# spells (name and link to detail page)
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
# pbar = tqdm(total=2650, desc="[Processing]", unit=" spell")
cpt = 0

for li in lis: # now we loop over all spells, get the page link and scrap all attributes
    url = li.a['href']

    ## get html of details page
    responseDetails = requests.get(url)
    spellSoup = BeautifulSoup(responseDetails.content, 'lxml')

    # get article content which contains all info about the spell
    spellContent = spellSoup.find(id='article-content')
    # pbar.update(1)

###################
### ATTRIBUTES
###################

    # get name
    if spellContent :
        spell_name = spellContent.find('h1').text
    else :
        spell_name = None
        continue
    print("name: ",spell_name)

    # get school and level
    school_levels = spellContent.find('b',string="School").find_previous('p')
    text = school_levels.text
    parts = text.split("Level")
    spell_school = parts[0].replace("School","").strip().strip(";")
    spell_level = parts[1].replace("Level","").strip().split(";")[0]

    # print("School: ",spell_school)
    # print("Level:",spell_level)

    # get casting time
    castTime = []
    spell_castTime = spellContent.find('b',string="Casting Time")
    spell_castTime = getStringSiblings(castTime, spell_castTime, 'b')
    # print("Cast time: ", spell_castTime)

    # get components 
    components = []
    spell_components = spellContent.find('b', string='Components')#.next_sibling.strip()
    spell_components = getStringSiblings(components, spell_components, 'p')
    # print ("Components: ", spell_components)

    # get range
    rangesp = []
    spell_range = spellContent.find('b',string="Range")
    spell_range = getStringSiblings(rangesp, spell_range, 'b')
    # print("Range: ", spell_range)

    # get target
    target = []
    spell_target = spellContent.find('b',string="Target")
    spell_target = getStringSiblings(target, spell_target, 'b')
    # print("Target: ", spell_target)

    #get duration
    duration = []
    spell_duration = spellContent.find('b',string="Duration")
    spell_duration = getStringSiblings(duration, spell_duration, 'b')
    # print("Duration: ",spell_duration)

    
    # get saving throw
    svthrow = []
    spell_saving_throw = spellContent.find('b',string='Saving Throw')
    spell_saving_throw = getStringSiblings(svthrow, spell_saving_throw, 'b')
    # print("Saving throw: ", spell_saving_throw)

    # get resistance
    resistance = []
    spell_resistance = spellContent.find('b',string='Spell Resistance')
    spell_resistance = getStringSiblings(resistance, spell_resistance, 'b')
    # print("Spell Resistance: ", spell_resistance)

    # get area
    area = []
    spell_area = spellContent.find('b',string='Area')
    spell_area = getStringSiblings(area, spell_area, 'b')
    # print("Area:", spell_area )

    # get effect
    effect = []
    spell_effect = spellContent.find('b',string='Effect')
    spell_effect = getStringSiblings(effect, spell_effect, 'b')
    # print('Effect: ',spell_effect)

    # get description 
    description = spellContent.find('p', string='DESCRIPTION')
    if(description):
        next_elem = description.find_next_sibling()
    html = ''
    while next_elem and not (next_elem.name == 'div' and 'section15' in next_elem.get('class', [])):
        html += str(next_elem)
        next_elem = next_elem.find_next_sibling()

    # Convert HTML string to regular string
    htmlString = str(html)

    if "<h4" in htmlString:
        # Trim HTML string
        htmlString = htmlString.split("<h4")[0]

    if "</p><div>" in htmlString:
        last_p_index = htmlString.rfind("</p>")

        if last_p_index != -1:
            htmlString = htmlString[:last_p_index + 4]

    # Convert back to BeautifulSoup object
    spell_paragraphs = htmlString

    # add all attributes to a spell dictionnary
    spellz[spell_name] = {
        'school': spell_school,
        'level': spell_level,
        'casting_time': spell_castTime,
        'components': spell_components,
        'range': spell_range,
        'target': spell_target,
        'duration': spell_duration,
        'saving_throw': spell_saving_throw,
        'spell_resistance': spell_resistance,
        'area': spell_area,
        'effect': spell_effect,
        'description': spell_paragraphs
    }

with open('outputs/spells.yaml', 'w') as f:
    yaml.dump(spellz, f)

# pbar.close() 

    

   




