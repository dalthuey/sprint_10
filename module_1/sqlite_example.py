import sqlite3
import queries as q
import pandas as pd

# step 1 - CONNECTION
def connect_to_db(db_name= 'rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_q(conn, query):
    # step 2 - CURSOR
    curs = conn.cursor()

    # step 3 - EXECUTE
    curs.execute(query)

    # step 4 - PULL
    return curs.fetchall()

if __name__ == '__main__':
    conn = connect_to_db()
    # print(execute_q(conn, q.SELECT_ALL)[:5])
    results = execute_q(conn, q.AVG_ITEM_WEIGHT_PER_CHARACTER)
    df = pd.DataFrame(results)
    df.columns = ['name', 'average-item-weight']
    df.to_csv('rpg_db.csv', index= False)