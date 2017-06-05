from Model.connection import *

class Answer:


    def selectByQuestionId(q_id):
        cursor.execute( "SELECT * FROM 	Answers WHERE question_id="+str(q_id) );
        data = cursor.fetchall();
        return data

    def insert(questionID,ans):
        cursor.execute("""INSERT INTO Answers (question_id ,answer_text  ) VALUES (%s,%s)""",
                       (questionID, ans))
        conn.commit();
        if (cursor.rowcount > 0):
            return cursor.lastrowid
        else:
            return False