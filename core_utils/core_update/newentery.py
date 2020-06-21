from Tools.scripts.treesync import raw_input

class Registry:
    def __init__(self,cursor,db):
        self.cursor=cursor
        self.db=db

    def register(self):
        student_name = raw_input("enter the new student Name")
        roll_no=raw_input("enter the new roll no")
        self.new_student_details("\"" +roll_no+"\"","\""+student_name+"\"")

    def new_student_details(self,roll_no,student_name):
        print("new student_name = " + student_name + " " + "new roll_no= " + roll_no)
        self.cursor.execute(''' INSERT into student(roll_no, student_name) VALUES(?,?)''',(roll_no,student_name))
        # print("new student_name = " + student_name + " " + "new roll_no= " + roll_no)
        self.db.commit()





