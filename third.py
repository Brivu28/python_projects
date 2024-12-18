import sqlite3

con = sqlite3.connect('youtube.db')

cursor = con.cursor()

cursor.execute('''
               Create table if not exists videos(
                   id INTEGER PRIMARY KEY,
                   name VARCHAR NOT NULL,
                   time VARCHAR
               )
               ''')
def listt():
    cursor.execute('''select * from videos''')
    for i in cursor.fetchall():
        print(i)
    con.commit()
def addV(name,time):
    cursor.execute('''
                   insert into videos (name,time)
                   values
                   (?,?)
                   ''',(name,time))
    con.commit()
def udt(id,name,time):
    cursor.execute('''
                   update videos
                   SET name = ?,
                   time = ?
                   WHERE id = ?
                   ''',(name,time,id))
    con.commit()
def delt(id):
    cursor.execute('''delete from videos
                   WHERE id = ?''',(id,))
    con.commit()
def main():
    while True:
        print("\n Youtube Manager")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit")
        
        ch = int(input("Enter The Choice:-\t"))
        
        if (ch == 1):
            listt()
        if (ch == 2):
            name = input("Enter The Video Name:- ")
            time = input("Enter The Video time:- ")
            addV(name,time)
        if (ch == 3):
            id = int(input("Enter The Id Of The Video:-  "))
            name = input("Ente The Name OF The Video:- ")
            time = int(input("Enter The Time :-"))
            udt(id,name,time)
        if(ch == 4):
            id = int(input("Enter The Id of The Video:- "))
            delt(id)
        if (ch==5):
            break
if __name__ == "__main__":
    main()