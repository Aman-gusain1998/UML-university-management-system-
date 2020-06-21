import sqlite3
from core_utils.ums_utils.student import Student
from core_utils.ums_utils.teacher import Teacher
from core_utils.ums_utils.college import College
from core_utils.ums_utils.university import University
from mailer import Mailer
from mailer import Message
from core_utils.core_update.update import Update
from core_utils.core_update.newentery import Registry
class UniversityManagementSystem:
    def __init__(self):
        # print("########## UniversityManagementSystem ############ ")
        db = sqlite3.connect(':memory:')
        db = sqlite3.connect('C:\\Users\\Aman\\PycharmProjects\\UnversityManagementSystem\\information')
        self.cursor = db.cursor()
        self.db=db

    def studentDetails(self):
        id,name,branch,gender=Student(self.cursor).get_student_details("\""+self.student_roll_no+"\"")
        return id,name,branch,gender
    def teacherDetails(self):
        name,department=Teacher(self.cursor).get_teacher_details("\""+self.student_roll_no+"\"")
        return name,department

    def collegeDetails(self):
        name,location = College("\""+self.student_roll_no+"\"",self.cursor).get_college_details()
        return name,location

    def universityDetails(self):
        name,location,iso = University("\""+self.student_roll_no+"\"",self.cursor).get_university_details()
        return name,location,iso

    def print_details(self):

        student_id,student_name,student_branch,student_gender=self.studentDetails()
        print ("Student ID is :- "+self.formatter(student_id))
        print ("Student Name is :- "+self.formatter(student_name))
        print ("Student Branch is :- "+self.formatter(student_branch))
        print ("Gender is :- "+self.formatter(student_gender))
        teacher_name,teacher_department = self.teacherDetails()
        print ("Associated teacher name is :- "+self.formatter(teacher_name))
        print ("Associated teacher department:- "+self.formatter(teacher_department))
        college_name,college_location = self.collegeDetails()
        print ("Student college name is :- "+self.formatter(college_name))
        print ("Student college location is "+self.formatter(college_location))
        university_name,university_location,university_iso = self.universityDetails()
        print ("Name of the university is :- "+self.formatter(university_name))
        print ("University Location is :- "+self.formatter(university_location))
        print ("ISO:9001 Certified "+self.formatter(university_iso))

        # print("1.) get student details", studentDetails(self))
        # print("2.) get update details", update(self.cursor).update_details(self))
    # print("3.) register new details")

    def formatter(self,value):
        formatted_value=str(value).strip("',)]").strip("[(u'")
        return formatted_value

    def emailSender(self):
        message = Message(From="ahujadeepanshu494@gmail.com",
                          To=["deepanshu.ahuja@guavus.com"],
                          Subject="University Management System")
        message.Body = """UMS deepanshu ahuja"""
        # message.attach("kitty.jpg")

        sender = Mailer('smtp.example.com')
        sender.send(message)

    def main_menu(self):
        print("1.)Get the student details")
        print("2. Update the student Details")
        print("3.) Register the new student ")

        option = int(input("Enter your choice"))
        if (option == 1):
            self.student_roll_no = str(input("Enter the student roll no."))
            self.print_details()
        elif (option == 2):
            self.student_roll_no = str(input("Enter the student roll no."))
            self.update_details()
        elif (option==3):
            self.register()

    def update_details(self):
         Update(self.cursor, self.db).update_details("\"" + self.student_roll_no + "\"")

    def register(self):
           Registry(self.cursor,self.db).register()
#

ums = UniversityManagementSystem()
# ums.print_details()
ums.main_menu()
# ums.update_details()