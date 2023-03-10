# This file was used for debbuging purposes.
# It helped testing attributes separetly in 
# order to better parse them or to optimize/
# factor some code.

import urllib.request 
import requests
import bs4
from bs4 import BeautifulSoup
from lxml import html

URL = "https://www.d20pfsrd.com/magic/all-spells/a/ant-haul/"

responseDetails = requests.get(URL)
spellSoup = BeautifulSoup(responseDetails.content, 'lxml')
spellContent = spellSoup.find(id='article-content')

def parseLevelAndGetClass(spell_level):
    class_dict = {}
    for class_level in spell_level.split(","):
        class_level = class_level.strip()
        if " " in class_level:
            class_name, level = class_level.rsplit(maxsplit=1)
            if "/" in class_name:
                class_names = class_name.split("/")
                for name in class_names:
                    class_dict[name.strip()] = level.strip()
            else:
                class_dict[class_name.strip()] = level.strip()
        else:
            class_dict[class_level.strip()] = "1"
    return class_dict

###################
### LEVELS
###################
school_levels = spellContent.find('b',string="School").find_previous('p')
text = school_levels.text
parts = text.split("Level")
spell_school = parts[0].replace("School","").strip().strip(";")
spell_level = parts[1].replace("Level","").strip().split(";")[0]

print("level: ", spell_level)
print("school: ", spell_school)

class_levels = parseLevelAndGetClass(spell_level)
print(class_levels)

###################
### DESCRIPTION
###################
# spell_description = spellContent.find('p',string='DESCRIPTION')
# print("Desc separator: ", spell_description)      

# spell_paragraphs = []
# spell_description = spellContent.find('p',string='DESCRIPTION')
# if not spell_description:
#     spell_description = spellSoup.find('div', {'class': 'page-center'}).find('p',string='DESCRIPTION')
# spell_description = spell_description.find_next('p')

# while spell_description and not spell_description.find_previous('div', {'class': 'section15'}):
#     if spell_description.has_attr('class'):
#         spell_paragraphs.append(spell_description.text)
#     else:
#         spell_paragraphs.append(spell_description.text)
#     spell_description = spell_description.find_next('p')
#     if spell_description and spell_description.parent.name == 'div':
#         break

# print("Spell description:\n", '\n\n'.join(spell_paragraphs))

# def getStringSiblings(array, content, stop):
#     if content:
#         for sibling in content.next_siblings:
#             print(sibling)
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