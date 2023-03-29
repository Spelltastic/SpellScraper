# This file was used for debbuging purposes.
# It helped testing attributes separetly in 
# order to better parse them or to optimize/
# factor some code.

import urllib.request 
import requests
import bs4
from bs4 import BeautifulSoup
from lxml import html

# URL = "https://www.d20pfsrd.com/magic/all-spells/m/magic-circle-against-evil/"
# URL = "https://www.d20pfsrd.com/magic/all-spells/p/prophetic-lore/"
URL = "https://www.d20pfsrd.com/magic/all-spells/t/time-stop/"

responseDetails = requests.get(URL)
spellSoup = BeautifulSoup(responseDetails.content, 'lxml')
spellContent = spellSoup.find(id='article-content')

description = spellContent.find('p', string='DESCRIPTION')

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
trimmed_html = BeautifulSoup(htmlString, 'html.parser')
str(trimmed_html)
trimmed_html.prettify()
print(trimmed_html)

###################
### LEVELS
###################
# school_levels = spellContent.find('b',string="School").find_previous('p')
# text = school_levels.text
# parts = text.split("Level")
# spell_school = parts[0].replace("School","").strip().strip(";")
# spell_level = parts[1].replace("Level","").strip().split(";")[0]

# print("level: ", spell_level)
# print("school: ", spell_school)

###################
### DESCRIPTION
###################
# spell_paragraphs = []
# spell_description = spellContent.find('p',string='DESCRIPTION')
# if not spell_description:
#     spell_description = spellSoup.find('div', {'class': 'page-center'}).find('p',string='DESCRIPTION')
# if not spell_description:
#     spell_description = None
#     exit # change to continue
# spell_description = spell_description.find_next()
# # check if spell description is a table
# if spell_description.name == 'table':
#     spell_paragraphs.append(spell_description)
# spell_description = spell_description.find_next()

# print("paragraphs: ", spell_paragraphs)
# print("description: ", spell_description)
# Find the parent tag of the <p> tag with text "DESCRIPTION"


# prettify


###################
### TARGET
###################
# target = []
# spell_target = spellContent.find('b',string="Target")
# spell_target = getStringSiblings(target, spell_target, 'b')
# print("Target: ", spell_target)

# def getDescription(array, content):
#     if content:
#         content = content.find_next()
#         array.append(content.text)
#         if 

# def getStringSiblings(array, content, stop):
#     if content:
#         for sibling in content.next_siblings:
#             if sibling.name == stop:
#                 break
#             if sibling.name == 'a':
#                 array.append(sibling.text)
#             elif isinstance((sibling), bs4.element.NavigableString):
#                 component_text = sibling.string.strip()
#                 if component_text:
#                     array.append(component_text.rstrip(';'))
#     else:
#         return None
#     return ' '.join(array)

###################
### DURATION
###################

# spell_duration = spellContent.find('b',string='Duration')
# if spell_duration:
#     if spell_duration.next_sibling is not None:
#         spell_duration = spell_duration.next_sibling.text.strip()
#     else :
#         print("fix here ---")
#         print("first: ", spell_duration)
#         spell_duration = spell_duration.find_next('br')
#         print(spell_duration)
# else :
#     spell_duration = None
# print("Duration: ",spell_duration)
# print("Duration: ",spell_duration)