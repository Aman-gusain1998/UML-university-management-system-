class Teacher:
    def __init__(self,cursor):
        self.cursor=cursor

    def get_teacher_name(self,roll_no):
        self.cursor.execute("select teacher_name from teacher where student_roll_no="+roll_no)
        teachername=self.cursor.fetchall()
        return teachername

    def get_teacher_department(self,roll_no):
        self.cursor.execute("select teacher_department from teacher where student_roll_no="+roll_no)
        teacherdepartment=self.cursor.fetchall()
        return teacherdepartment


    def get_t_u_id(self,roll_no):
        self.cursor.execute("Select t_u_id from teacher where student_roll_no=" + roll_no)
        teacher_university_id = self.cursor.fetchall()
        return teacher_university_id

    def get_t_c_id(self,roll_no):
        self.cursor.execute("Select t_c_id from teacher where student_roll_no="+roll_no)
        teacher_college_id =self.cursor.fetchall()
        return teacher_college_id

    def get_teacher_details(self,teacher_id):
        name = self.get_teacher_name(teacher_id)
        department = self.get_teacher_department(teacher_id)
        return name, department
