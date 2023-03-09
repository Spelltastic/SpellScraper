# Spell Scrapper :scroll: :snake:

## About this repository
This repository was built in order to have an "up to date" spells database for [SpellTastic](https://codefirst.iut.uca.fr/git/Spelltastic/Spelltastic), a cross-platform spell manager for Patfinder.

## Data source
All data is retrieved from [d20pfsrd](https://www.d20pfsrd.com/) the __#1 Pathfinder Roleplaying Game rules reference site__. All spells can be found at [spells](https://www.d20pfsrd.com/magic/all-spells/).

The latest data extracted is available as a YAML file.

## Getting Started

### Prerequisites
* Python 3.6+

#### Python libraries
* BeatifulSoup4
* Requests
* lxml
* PyYAML
* sqlite3
  
### Installing 
1. Cloning repository
```
git clone https://github.com/your_username/pathfinder-spell-scraper.git
```
2. Install the required libraries
```
pip install requests beautifulsoup4 lxml pyyaml
```

## Usage 

### Scrapping 
3. You can run __scrap-spells.py__ to scrape the spell information from the website:
```
python3 scrap-spells.py
```
__The script should take a few minutes to scrap all spells__

4. This command will generate a file __spells.yaml__ with all spells and their attributes

### Database
5. You can build a __.db__ sqlite3 databse file by running the __spell_db.py__ file:
```
python3 spell-db.py
```

6. The script will create a __spells.db__ file with a spell table containing all the spell information.
