from Model.connection import *

class correctAnswer:


    def selectByQuestionId(q_id):
        cursor.execute( "SELECT * FROM 	correctAnswer WHERE question_id ="+str(q_id) );
        data = cursor.fetchall();
        return data

    def insert(questionID,ansID):
        cursor.execute("""INSERT INTO correctAnswer (question_id  ,correct_ans_id   ) VALUES (%s,%s)""",
                       (questionID, ansID))
        conn.commit();
        if (cursor.rowcount > 0):
            return cursor.lastrowid
        else:
            return False