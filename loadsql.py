import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

with open('SQL/mis.sql', encoding='utf-8') as f:
 for line in f:
  if line.startswith('insert'):
   table_name = line.split()[2].split('(')[0].strip('`')
   print("Cleaning data ... " + table_name )
   cur.execute('DELETE FROM ' + table_name)
   cur.executescript(line)
con.commit()
con.close()