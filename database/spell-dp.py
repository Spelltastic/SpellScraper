import yaml
import sqlite3

def createDatabase():
    connexion = sqlite3.connect('outputs/spells.db')
    cursor = connexion.cursor()

    cursor.execute('''DROP TABLE IF EXISTS spell''')
    cursor.execute('''CREATE TABLE spell(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        level TEXT,
        school TEXT,
        casting_time TEXT,
        components TEXT,
        range TEXT,
        target TEXT,
        area TEXT,
        effect TEXT,
        duration TEXT,
        saving_throw TEXT,
        spell_resistance TEXT,
        description TEXT)''')

    connexion.commit()
    connexion.close()

def insertSpells():
    with open('outputs/spells.yaml', 'r') as file:
        spells = yaml.safe_load(file)

    connexion = sqlite3.connect('outputs/spells.db')
    cursor = connexion.cursor()
    
    for name, spell in spells.items():
        level = spell.get('level')
        school = spell.get('school')
        casting_time = spell.get('casting_time')
        range_ = spell.get('range')
        target = spell.get('target')
        duration = spell.get('duration')
        saving_throw = spell.get('saving_throw')
        spell_resistance = spell.get('spell_resistance')
        description = '\n'.join(spell.get('description', []))
        components = spell.get('components')
        area = spell.get('area')
        effect = spell.get('effect')

        cursor.execute('''INSERT INTO spell(name, level, school, casting_time, components, range, target, area, effect, duration, saving_throw, spell_resistance, description) 
                       VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                       (name, level, school, casting_time, components, range_, target, area, effect, duration, saving_throw, spell_resistance, description))

    connexion.commit()
    connexion.close()

createDatabase()
insertSpells()