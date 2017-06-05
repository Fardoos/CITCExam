from pymysql import connect, err, sys, cursors

# def connectionDB(self):
conn = connect(host='localhost',
                       user='root',
                       passwd='iti',
                       db='Courses_Exam');
cursor = conn.cursor(cursors.DictCursor);