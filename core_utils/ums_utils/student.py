class Student:
    def __init__(self,cursor):
        self.cursor=cursor

    def get_student_id(self,roll_no):
        self.cursor.execute("Select student_id from student where roll_no=" + roll_no)
        studentid=self.cursor.fetchall()
        return studentid

    def get_student_name(self,roll_no):
        self.cursor.execute("Select student_name from student where roll_no=" + roll_no)
        studentname = self.cursor.fetchall()
        return studentname

    def get_student_branch(self,roll_no):
        self.cursor.execute("Select student_branch from student where roll_no=" + roll_no)
        studentbranch=self.cursor.fetchall()
        return studentbranch

    def get_student_gender(self,roll_no):
        self.cursor.execute("Select student_gender from student where roll_no="+roll_no)
        studentgender=self.cursor.fetchall()
        return studentgender


    def get_student_details(self,roll_no):
        id = self.get_student_id(roll_no)
        name = self.get_student_name(roll_no)
        branch = self.get_student_branch(roll_no)
        gender = self.get_student_gender(roll_no)
        return id,name,branch,gender

    # @classmethod
    # def update_details(cls, param, param1, param2, param3, param4, param5):
    #    pass