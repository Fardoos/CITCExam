from Model.connection import *

class Chapter:


    def selectChapter(self):
        cursor.execute( "SELECT * FROM 	Chapters " );
        data = cursor.fetchall();
        return data
        #print( data );

    def selectChapterByCourseId(c_id):
        cursor.execute( "SELECT * FROM 	Chapters  WHERE course_id="+str(c_id) );
        data = cursor.fetchall();
        return data
        #print( data );
    def selectChapterID(c_id,list_of_ids):
        format_strings = ','.join(['%s'] * len(list_of_ids))
        cursor.execute( "SELECT id FROM Chapters  WHERE course_id="+str(c_id)+" AND chapter_num IN (%s)" % format_strings,
                        list_of_ids );
        data = cursor.fetchall();
        return data

    def insert(courseID,chapterNum):
        cursor.execute("""INSERT INTO Chapters (course_id ,chapter_num ) VALUES (%s,%s)""",
                       (courseID, chapterNum))
        conn.commit();
        if (cursor.rowcount > 0):
            return cursor.lastrowid
        else:
            return False






m=Chapter

#print(m.insert("test2",2))
