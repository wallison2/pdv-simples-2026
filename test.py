import sqlite3

conn = sqlite3.connect("licencas_local.db")
c = conn.cursor()
c.execute("SELECT * FROM pool_hmac LIMIT 10")
for row in c.fetchall():
    print(row)
conn.close()
