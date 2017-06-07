
from Model.connection import *


class Course:


    def selectCourses(self):
        cursor.execute( "SELECT * FROM 	Courses " );
        data = cursor.fetchall();
        return data
        #print( data );
    def selectChapterNum(c_id):
        cursor.execute( "SELECT * FROM 	Courses WHERE id="+str(c_id) );
        data = cursor.fetchall();
        return data
        #print( data );

    def insert( name,chapterNum):
        cursor.execute("""INSERT INTO Courses (course_name ,chapter_nums) VALUES (%s,%s)""",
                       (name, chapterNum))
        conn.commit();
        if (cursor.rowcount > 0):
            return cursor.lastrowid
        else:
            return False

    def delete( c_id):
        cursor.execute("DELETE FROM Courses WHERE id="+str(c_id))

        conn.commit();


m=Course

#print(m.insert("test2",2))
