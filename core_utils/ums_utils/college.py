from core_utils.ums_utils.teacher import Teacher
class College:
    def __init__(self,roll_no,cursor):
        self.t_c_id=str(Teacher(cursor).get_t_c_id(roll_no)).split(",")[0].strip("[(u")
        self.cursor=cursor

    def get_college_name(self):
        self.cursor.execute("Select college_name from college where t_c_id=" + self.t_c_id)
        college_name=self.cursor.fetchall()
        return college_name

    def get_college_location(self):
        self.cursor.execute("Select college_location from college where t_c_id=" + self.t_c_id)
        college_location = self.cursor.fetchall()
        return college_location


    def get_t_c_id(self, college_id):
        self.cursor.execute("Select t_c_id from college where college_id=" + college_id)

    def get_college_details(self):
        name = self.get_college_name()
        location = self.get_college_location()
        return name,location

