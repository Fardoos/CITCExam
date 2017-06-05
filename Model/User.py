from Model.connection import *



class User:
    def selectUser(email):
        cursor.execute("SELECT user_name FROM Users WHERE email=%s ", (email))
        username = cursor.fetchall();
        return username;


    def selectName(email):
        data = cursor.execute("SELECT * FROM Users WHERE email=%s", (email))
        data = cursor.fetchall()
        return data



    def selectbyemail(email, password):
        data = cursor.execute("SELECT * FROM Users WHERE email=%s and password=%s", (email, password))
        # print(data);
        if (data > 0):
            return email
        else:
            return False

    def insertInto(u_name, email, password):
        cursor.execute("""INSERT INTO Users (user_name,email,password) VALUES (%s,%s,%s)""",
                       (u_name, email, password))
        conn.commit();
        if (cursor.rowcount > 0):
            return cursor.lastrowid
        else:
            return False

    def updateUser(u_id, u_name, email, password):
        cursor.execute("""UPDATE Users set u_name =%s,email=%s, password=%s WHERE u_id=%s""",
                       (u_name, email, password, u_id))
        conn.commit()
        print(cursor.rowcount)




user=User;

#print(user.insertInto("admin","admin","admin"))
