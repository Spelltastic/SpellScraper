# Spell Scrapper :scroll: :snake:

## About this repository
This repository was built in order to have an "up to date" spells database for [SpellTastic](https://codefirst.iut.uca.fr/git/Spelltastic/Spelltastic), a cross-platform spell manager for Pathfinder.

## Data source
All data is retrieved from [d20pfsrd](https://www.d20pfsrd.com/) the __#1 Pathfinder Roleplaying Game rules reference site__. All spells can be found at [spells](https://www.d20pfsrd.com/magic/all-spells/).

The latest data extracted is available as a YAML file and can be found in the `outputs` directory.

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
python scrapping/scrap-spells.py
```

4. This command will generate a file __spells.yaml__ with all spells and their attributes. The file should be found in the `outputs` directory.  

_A progress bar should be displayed in your terminal while scrapping, showing the time left and the number of spells scraped. The script should takes about 20 minutes to scrap all spells._

### Database
5. You can build a __.db__ sqlite3 databse file by running the __spell_db.py__ file:
```
python database/spell-db.py
```

6. The script will generate a __spells.db__ file with a spell table containing all the spell information. This file should also be found in the `outputs` directory.
