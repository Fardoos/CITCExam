from tornado import web,ioloop
from Model import Course
from tkinter import messagebox
import tkinter as tk
root = tk.Tk()
root.withdraw()
# to use ajax
import sys
import json
import cgi
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