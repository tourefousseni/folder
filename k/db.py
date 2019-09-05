import psycopg2
# connect to the database

con = psycopg2.connect(
    host="localhost",
    database="kala1",
    user="fulani",
    password="tourefousseni1",)

# the cursor
cur = con.cursor()

#cur.execute("insert into k_person(id, prenom) values (%s, %s)", (4, "fili"))
# execute query
cur.execute("select * from k_person")

rows = cur.fetchall()
for r in rows:
    print(f" {r[0]} {r[1]} {r[2]} ")


# close the connection
con.close()