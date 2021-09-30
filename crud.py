import mysql.connector
import os

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='gconus5226',
    database="meme_generator"
)

def check_name(db, name) :
    cursor = db.cursor()
    sql_check_name = "SELECT * FROM user WHERE name = %s"
    valname = (name,)
    cursor.execute(sql_check_name, valname)

    results = cursor.fetchall()
    if cursor.rowcount > 0 :
        user_id = results[0][0]
        name = results[0][1]
        email = results[0][2]
        password = results[0][3]
        return True, user_id, name, email, password
    return False

def insert_data(db) :
    name = input("Insert name : ")
    email = input ("Insert Email : ")
    password = input("Insert Password : ")
    val = (name, email, password)

    cursor = db.cursor()

    if check_name(db, name)[0] == True :
        print("Input another name")
        return
    
    sql = "INSERT INTO user (name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("Data Added!!")

def get_data(db) :
    cursor = db.cursor()
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0 :
        print("There's no data in table")
    else :
        for data in results :
            print(data)

def update_data(db) :
    cursor = db.cursor()
    get_data(db)
    user_name = input ("Insert user name : ")
    results = check_name(db, user_name)
    if  results == False :
        print("Name not found")
        return

    name = input("New name : ")
    email =  input ("New email : ")
    password = input ("New password : ")

    if name == "" :
        name = results[2]
    if email == "" :
        email = results[3]
    if password == "" :
        password = results[4]

    sql = "UPDATE user SET name = %s, email = %s, password = %s WHERE user_id = %s"
    val = (name, email, password, results[1])
    cursor.execute(sql, val)
    db.commit()
    print("Data updated!!!")

def delete_data(db) :
    cursor = db.cursor()
    get_data(db)
    user_name = input ("Insert user name : ")
    results = check_name(db, user_name)
    if  results == False :
        print("Name not found")
        return
    
    sql = "DELETE FROM user WHERE user_id = %s"
    val = (results[1],)
    cursor.execute(sql, val)
    db.commit()
    print("Data deleted!!!")

def search_data(db) :
    cursor = db.cursor()
    user_name = input("Insert name : ")
    sql = "SELECT * FROM user WHERE name = %s"
    val = (user_name,)
    cursor.execute(sql, val)
    results = cursor.fetchall()
    if cursor.rowcount > 0 :
        print(results[0])
        return
    print("Data not found")

def show_menu(db):
    print("====== APLIKASI DATABASE PYTHON ======")
    print("1. Insert Data")
    print("2. Get Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Search Data")
    print("0. Exit")
    print("----------------")
    menu = input("Select one menu : ")

    #clear screen
    os.system("clear")

    if menu == "1":
        insert_data(db)
    elif menu == "2":
        get_data(db)
    elif menu == "3" :
        update_data(db)
    elif menu == "4" :
        delete_data(db)
    elif menu == "5" :
        search_data(db)
    elif menu == "0" :
        exit()
    else :
        print("Wrong menu!!!") 

if __name__ == "__main__" :
    while(True):
        show_menu(db)