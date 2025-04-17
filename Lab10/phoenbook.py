import psycopg2,csv

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Dund@r07",
    host="localhost"
)
cur = conn.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            phone VARCHAR(15) NOT NULL
);
""")

n = 0

choise = int(input("1-to insert user , 2-for delete user , 3-to change number :"))



if choise == 1:

    name = input("Enter your full name: ")
    phone = input("Enter your phone: ")

    cur.execute("INSERT INTO phonebook (full_name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()

elif choise == 2:

    name_to_delete = input("Enter name to delete: ")
    cur.execute("DELETE FROM phonebook WHERE full_name = %s", (name_to_delete,))
    conn.commit()
elif choise == 3:
    update = input("Enter name to update number: ")
    new_phone = input("Enter the number: ")
    cur.execute("update phonebook set phone = %s where full_name = %s",(new_phone,update))

cur.execute("SELECT setval(pg_get_serial_sequence('phonebook', 'id'), max(id)) FROM phonebook;")
conn.commit()


filt = int(input("filter by name(0) or by id(1): "))
if filt == 0:
    cur.execute("""SELECT * FROM phonebook ORDER BY full_name ASC""") 
    rows = cur.fetchall()
    conn.commit()
elif filt == 1:
    cur.execute("""SELECT * FROM phonebook ORDER BY id ASC""") 
    rows = cur.fetchall()
    conn.commit()
print("id | name | phone")
for row in rows:
    print(f"{row[0]} | {row[1]} | {row[2]}")

with open('phonebookk.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    cur.execute("""SELECT * FROM phonebook""") 
    rows = cur.fetchall()
    conn.commit()

    writer.writerows(rows)
# Закрытие соединения
cur.close()
conn.close()
