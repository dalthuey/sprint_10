import sqlite3

# step 1 - CONNECTION
connection = sqlite3.connect('rpg_db.sqlite3')

# step 2 - CURSOR
cursor = connection.cursor()

# step 3 - QUERY
query = 'SELECT character_id, name FROM charactercreator_character;'

# step 4 - EXECUTE
results = cursor.execute(query).fetchall()

if __name__ == '__main__':
    print(results[:5])
