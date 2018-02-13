import sqlite3

conn = sqlite3.connect('tutorial.db')
cur = conn.cursor()

def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,'
                ' datestamp TEXT, keyword TEXT, value REAL)')
def data_entry():
    cur.execute("INSERT INTO stuffToPlot VALUES(145123542, "
                "'2018-01-01', 'Python', 5)")
    conn.commit()
    cur.close()
    conn.close()

create_table()
data_entry()