import psycopg2,csv
import re 
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
            full_name VARCHAR(50) NOT NULL,
            phone VARCHAR(15) NOT NULL
);
""")

# n = 0
# lst = []
# print( bool(lst))

def search(pattern):
    cur.callproc('search', (pattern,))
    res = cur.fetchall()
    for row in res:
        print(row)

search("Serdar")


def multiple_users(names,phones):
    phone_correct = r'^\+?\d{8,15}'

    invalidnames = []
    invalidphones = []

    if len(names) != len(phones):
        raise ValueError("Names and phones arrays have different lengths")
    for i in range(len(names)):
        name = names[i]
        phone = phones[i]

        if not re.match(r'^[A-Za-z]+$', name):
            invalidnames.append(name)
        # Проверяем номер телефона
        elif not re.match(phone_correct, phone):
            invalidphones.append(phone)
        else:
            cur.execute("SELECT 1 FROM phonebook WHERE full_name = %s AND phone = %s",(name,phone))
            exist = cur.fetchone()

            if exist:
                print(f"User {name} with phone {phone} already exists")
            else:
                cur.execute("INSERT INTO phonebook (full_name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    return invalidnames, invalidphones


names = ['Beq','Nurasyl','Anel','Dariya','Assel','Serdar7','hello']
phones = ['+123456789123','+789456132789','+654321987654','+321654987321','+9876543','+77777777777777','654654654546546']

invalidnames, invalidphones = multiple_users(names,phones)

print (f"invalid names:{invalidnames}, invalid phones:{invalidphones}")

def pagination(limit, offset):
    cur.callproc('queries',(limit,offset))
    
    rows = cur.fetchall()
    for row in rows:
        print (row)
pagination(3,2)



def delete_user_data(full_name=None, phone=None):
    
    cur.execute("CALL delete_user_data(%s, %s)", (full_name, phone))
    conn.commit()


delete_user_data(full_name = "hello")


def insert_or_update_contact(name,phone):
    
    cur.execute("SELECT full_name,phone FROM phonebook WHERE (full_name = %s) or (phone=%s)", (name,phone,))
    exists = cur.fetchall()
    rows = exists
    print (exists)
    for row in rows:
        print(f"{row[0]}: {row[1]}")
    
    
    
    if not exists:
        cur.execute("INSERT INTO phonebook (full_name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit() 
        return
    else:
         n = int(input("Which data to change? "))



    
    if exists[n-1][0] is not None and exists[n-1][1] is not phone:
       
 
        new_phone = input("Enter the number: ")
        cur.execute("update phonebook set phone = %s where full_name = %s",(new_phone,name))
        
        
    elif exists[n-1][1] is not None and exists[n-1][0] is not name:

        new_name = input("Enter the name: ")
        cur.execute("update phonebook set full_name = %s where phone = %s",(new_name,phone))
       
        

    conn.commit()


user = input("Enter your full name: ")
number = input("Enter your phone: ")
rows = search(user,number)
for row in rows:
    print(row)


insert_or_update_contact(user,number)


# choise = int(input("1-to insert user , 2-for delete user , 3-to change number :"))



# if choise == 1:

#     name = input("Enter your full name: ")
#     phone = input("Enter your phone: ")

#     cur.execute("INSERT INTO phonebook (full_name, phone) VALUES (%s, %s)", (name, phone))
#     conn.commit()
# elif choise == 2:

#     name_to_delete = input("Enter name to delete: ")
#     cur.execute("DELETE FROM phonebook WHERE full_name = %s", (name_to_delete,))
#     conn.commit()
# elif choise == 3:
#     update = input("Enter name to update number: ")
#     new_phone = input("Enter the number: ")
#     cur.execute("update phonebook set phone = %s where full_name = %s",(new_phone,update))

# cur.execute("SELECT setval(pg_get_serial_sequence('phonebook', 'id'), max(id)) FROM phonebook;")
# conn.commit()


# filt = int(input("filter by name(0) or by id(1): "))
# if filt == 0:
#     cur.execute("""SELECT * FROM phonebook ORDER BY full_name ASC""") 
#     rows = cur.fetchall()
#     conn.commit()
# elif filt == 1:
#     cur.execute("""SELECT * FROM phonebook ORDER BY id ASC""") 
#     rows = cur.fetchall()
#     conn.commit()
# print("id | name | phone")
# for row in rows:
#     print(f"{row[0]} | {row[1]} | {row[2]}")

# with open('phonebookk.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     cur.execute("""SELECT * FROM phonebook""") 
#     rows = cur.fetchall()
#     conn.commit()

#     writer.writerows(rows)
# Закрытие соединения
cur.close()
conn.close()
