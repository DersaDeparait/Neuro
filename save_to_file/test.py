import sqlite3

conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Создание таблицы
# cursor.execute("""CREATE TABLE el_huma(
#                     surname text,
#                     name text,
#                     age integer)""")

# cursor.execute("INSERT INTO el_huma VALUES ('Dog', 'Sufi', 74)")
# cursor.execute("INSERT INTO el_huma VALUES ('Dog', 'OXI', 700)")
# cursor.execute("INSERT INTO el_huma VALUES ('Dog', 'OXI', 0)")
# cursor.execute("INSERT INTO el_huma VALUES ('Dog', 'Kuki', 0)")
# cursor.execute("INSERT INTO el_huma VALUES ('Cat', 'Wiskas', 10)")

cursor.execute("INSERT INTO el_huma VALUES (?, ?, ?)", ("One", 'Two', 3))
cursor.execute("INSERT INTO el_huma VALUES (:1, :2, :3)", {"1":"Suk", "2":"Box", "3":45})

cursor.execute("SELECT * FROM el_huma WHERE surname = ?", ("Suk",))
cursor.execute("SELECT * FROM el_huma WHERE surname = :s", {"s":"One"})
# print(cursor.fetchall())
# print(cursor.fetchone())
print(cursor.fetchmany(2))

conn.commit()

conn.close()