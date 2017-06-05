from Model.connection import *

class Question:


    def selectQuestionById(c_id):

        cursor.execute( "SELECT id FROM 	Questions WHERE chapter_id IN (SELECT id FROM Chapters WHERE course_id="+str(c_id)+")" );
        data = cursor.fetchall();
        return data
         #print( data );

    def selectQuestionBychID(list_of_ids):
        format_strings = ','.join(['%s'] * len(list_of_ids))
        cursor.execute( "SELECT * FROM 	Questions WHERE chapter_id IN (%s)" % format_strings,
                        list_of_ids );

        data = cursor.fetchall();
        return data

    def insert(question,level,chapterID,objective):
        cursor.execute("""INSERT INTO Questions (quetion ,level ,chapter_id,objective  ) VALUES (%s,%s,%s,%s)""",
                       (question,level,chapterID,objective))
        conn.commit();
        if (cursor.rowcount > 0):
            return cursor.lastrowid
        else:
            return False






m=Question
print(m.selectQuestionById(1))
#m.insert("test")
