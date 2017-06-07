from tornado import web,ioloop,websocket
from Model import Course,Question,Answer,User,Chapter,correctAnswer
from tornado import web,ioloop,websocket
import random
# to find digit from string
import re
# An included library with Python3-tk install(for alert msg)
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()
# to use ajax
import sys
import json
import cgi




randomIDs=[]
simple_count = 0
difficult_count =0
reminding_count = 0
creativity_count = 0
understanding_count = 0


def generate_parent(length):
    #geneSet = [1,2,3,4,5,6,7,89,12,5,44,65,24,45,14,45,77,88,99,22]
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(randomIDs))
        genes.extend(random.sample(randomIDs, sampleSize))
    return genes

class Login(web.RequestHandler):
    def get(self):
        self.render("../View/login.html")
    def post(self):

        user=User
        email=self.get_argument("email")
        password=self.get_argument("password")
        login_user=user.User.selectbyemail(email,password)
        if(login_user==False):
            self.redirect("/login")
        else:
            self.set_cookie("mycookie",email)
            if email=="admin@admin":
                self.render('../View/dashboard.html')
            else:
                self.redirect("/")

class dashboard(web.RequestHandler):
    def get(self):

        self.render('../View/dashboard.html')


class SignUp(web.RequestHandler):
    def get(self):
        self.render('../View/signUp.html')
    def post(self):

        user=User
        u_name=self.get_argument("username")
        email=self.get_argument("email")
        password=self.get_argument("password")
        current_user=user.User.insertInto(u_name,email,password)
        self.set_cookie("mycookie", email)
        cookie = self.get_cookie("mycookie")
        self.redirect("/login")

class logout(web.RequestHandler):
    def get(self):
        self.clear_cookie("mycookie")
        self.redirect("/login")

class Home(web.RequestHandler):
    def get(self):
        if self.get_cookie("mycookie"):

            user = User
            username = user.User.selectUser(self.get_cookie("mycookie"))
            m = Course
            data=m.Course.selectCourses(m)
            self.render("../View/mainPage.html",courseName=data)
        else:
            self.redirect("/login")


class Exame(web.RequestHandler):
    def post(self):
        AnswerArray = []
        QuestionWithAns = {}
        ExameData = []

        questionData=Question
        answerData=Answer
        courseId = self.get_argument("courseID")
        data=questionData.Question.selectQuestionById(courseId)
        for qeu in data:
            answers=answerData.Answer.selectByQuestionId(qeu['id'])
            AnswerArray=[]
            for a in answers:
                AnswerArray.append(a['answer_text'])
            QuestionWithAns={qeu['quetion']:AnswerArray}
            ExameData.append(QuestionWithAns)
           # print(QuestionWithAns)
            #print(ExameData)
        self.render("../View/exam.html", data=ExameData)



class courseList(web.RequestHandler):
    def get(self):
        m = Course
        data = m.Course.selectCourses(m)
        # tk.messagebox._show("title","list courses")
        self.render("../View/courseList.html", courses=data)

class addCourse(web.RequestHandler):
    def get(self):
        self.render("../View/addCourse.html")

    def post(self):
        courseName = self.get_argument("courseName")
        chapterNumber = self.get_argument("chapterNumber")
        m = Course
        result= m.Course.insert(courseName,chapterNumber)
        if(result):
            tk.messagebox._show("course", "course added successfully")
            self.redirect("/courseList")
        else:
            tk.messagebox._show("course", "course not added")
            self.redirect("/addCourse")


class addQuestions(web.RequestHandler):
    def get(self):
        m = Course
        data = m.Course.selectCourses(m)
        self.render("../View/addQuestions.html",courses=data)

    def post(self):
        courseID = self.get_argument("courseID")
        chapterNumber = self.get_argument("chapterNumber")
        chapterID=Chapter.Chapter.insert(courseID,chapterNumber)
        if (chapterID):
            for i in range(12):
                quesion=self.get_argument("quesion"+str(i))
                ans1=self.get_argument("ans1"+str(i))
                ans2 = self.get_argument("ans2"+str(i))
                ans3 = self.get_argument("ans3"+str(i))
                correctAns=self.get_argument("correctAns"+str(i))
                level=self.get_argument("level"+str(i))
                objective=self.get_argument("objective"+str(i))
               # print(ans1+"---"+correctAns+"----"+ans2+"---"+ans3)
                quesionID=Question.Question.insert(quesion,level,chapterID,objective)
                if(quesionID):
                    answerID = Answer.Answer.insert(quesionID, ans1)
                    if(correctAns=="a"):
                        #print("ans1 correct")
                        correctAnswer.correctAnswer.insert(quesionID,answerID)

                    answerID = Answer.Answer.insert(quesionID, ans2)
                    if(correctAns=="b"):
                       # print("ans2 correct")
                        correctAnswer.correctAnswer.insert(quesionID, answerID)

                    answerID = Answer.Answer.insert(quesionID, ans3)
                    if(correctAns=="c"):
                        correctAnswer.correctAnswer.insert(quesionID, answerID)
                    # tk.messagebox._show("Questions", "Questions added successfully")
                else:
                    tk.messagebox._show("Questions", "something wrong")
        self.redirect("/courseList")


class addExame(web.RequestHandler):
    def get(self):
        m = Course
        data = m.Course.selectCourses(m)

        self.render("../View/addExame.html",courses=data)

    def post(self):
        AnswerArray = []
        QuestionWithAns = {}
        ExameData = []
        chapterIDsArray=[]
        # print(self.request.arguments['chapters']) checkbox array of values
        chapters=self.request.arguments['chapters']
        # print(re.findall('\d+', str(chapters)))
        chapterNums=re.findall('\d+', str(chapters))
        # if(self.get_argument("courseID")<=0):
        courseID = self.get_argument("courseID")
        chaptersIDs=Chapter.Chapter.selectChapterID(courseID,chapterNums)
        # print(chaptersIDs)
        for id in chaptersIDs:
            chapterIDsArray.append(id["id"])
        # print(chapterIDsArray)
        quesionsBank2=Question.Question.selectQuestionBychID(chapterIDsArray)
        quesionsBank=random.sample(quesionsBank2,12)
        print(quesionsBank)

        simple=self.get_argument("simple")
        difficult = self.get_argument("difficult")
        reminding = self.get_argument("reminding")
        understanding = self.get_argument("understanding")
        creativity = self.get_argument("creativity")
        # print(simple+"=="+difficult+"=="+reminding)

        simple_count=int(simple)
        difficult_count=int(difficult)
        reminding_count=int(reminding)
        creativity_count=int(creativity)
        understanding_count=int(understanding)
        resultArray=[]
        for question in quesionsBank:
            if question["level"]=="simple" and question["objective"]=="understand":
                if 0<simple_count<=int(simple) and 0<understanding_count<=int(understanding):
                    resultArray.append(question)
                    simple_count=simple_count-1
                    understanding_count=understanding_count-1



            elif question["level"]=="simple" and question["objective"]=="creativity":
                if 0<simple_count<=int(simple) and 0<creativity_count<=int(creativity):
                    resultArray.append(question)
                    simple_count=simple_count-1
                    creativity_count=creativity_count-1

            elif question["level"] == "simple" and question["objective"] == "reminding":
                if 0<simple_count<=int(simple) and 0<reminding_count<=int(reminding):
                    resultArray.append(question)
                    simple_count =simple_count-1
                    reminding_count =reminding_count-1




            elif question["level"] == "difficult" and question["objective"] == "understand":
                if 0<difficult_count<=int(difficult) and 0<understanding_count<= int(understanding):
                    resultArray.append(question)
                    difficult_count =difficult_count- 1
                    understanding_count =understanding_count- 1


            elif question["level"] == "difficult" and question["objective"] == "creativity":
                if 0<difficult_count<=int(difficult) and 0<creativity_count <= int(creativity):
                    resultArray.append(question)
                    difficult_count =difficult_count- 1
                    creativity_count =creativity_count- 1
                    print(simple_count)
                    print(difficult_count)
                    print(understanding_count)
                    print(reminding_count)
                    print(creativity_count)

            elif question["level"] == "difficult" and question["objective"] == "reminding":
                if 0<difficult_count<=int(difficult) and 0<reminding_count <= int(reminding):
                    resultArray.append(question)
                    difficult_count =difficult_count- 1
                    reminding_count =reminding_count- 1

        print(resultArray)
        for qeu in resultArray:
            answers=Answer.Answer.selectByQuestionId(qeu['id'])
            AnswerArray=[]
            for a in answers:
                AnswerArray.append(a['answer_text'])
            QuestionWithAns={qeu['quetion']:AnswerArray}
            ExameData.append(QuestionWithAns)
        self.render("../View/exam.html", data=ExameData)


class getChapters(web.RequestHandler):
    def post(self):
        courseid= self.get_argument("courseId")
        dict = {"c" : courseid}
        data=Chapter.Chapter.selectChapterByCourseId(courseid)
        dataDic={"data":data}
        # self.write(dataDic)
        self.write(json.dumps(data))
class getNumOfChapters(web.RequestHandler):
    def post(self):
        courseid= self.get_argument("courseId")
        myData=[]
        rangeCount=[]
        dict = {"c" : courseid}
        chapters=Chapter.Chapter.selectChapterByCourseId(courseid)
        chaptersCount=Course.Course.selectChapterNum(courseid);
        # print(chapters[0]['chapter_num']);
        # print(chaptersCount[0]["chapter_nums"]);
        for i in range(1,chaptersCount[0]["chapter_nums"]+1):
            rangeCount.append(i)
        print(rangeCount)

        for chaptNo in chapters:
            for i in rangeCount:
                print(i)
                if chaptNo['chapter_num']==i:
                    rangeCount.remove(i)


                print(rangeCount)
        print(rangeCount)
        dataDic={"data":rangeCount}
        self.write(json.dumps(rangeCount))

class deleteCourse(web.RequestHandler):
    def get(self,id):
        print(id)
        Course.Course.delete(id)
        self.redirect("/courseList")



app = web.Application([ (r"/", Home),
                        (r"/Exame",Exame),
                        (r"/login",Login),
                        (r"/signup",SignUp),
                        (r"/logout",logout),
                        (r"/courseList",courseList),
                        (r"/addCourse",addCourse),
                        (r"/addQuestions",addQuestions),
                        (r"/addExame",addExame),
                        (r"/delete/([0-9]+)",deleteCourse),
                        (r"/getChapters",getChapters),
                        (r"/dashboard",dashboard),
                        (r"/getNumOfChapters",getNumOfChapters)

                        ],debug=True,static_path='../static')


app.listen(7777)
ioloop.IOLoop.current().start()