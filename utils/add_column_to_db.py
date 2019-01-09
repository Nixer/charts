import sqlite3

conn = sqlite3.connect("webapp.db")
c = conn.cursor()
addColumn = "ALTER TABLE track ADD COLUMN words INT NULL"
c.execute(addColumn)
conn.commit()
c.close()
conn.close()
