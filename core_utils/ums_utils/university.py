from core_utils.ums_utils.teacher import Teacher

class University:
    def __init__(self,roll_no,cursor):
        self.t_u_id = str(Teacher(cursor).get_t_u_id(roll_no)).split(",")[0].strip("[(u")
        self.cursor=cursor

    def get_university_name(self):
        self.cursor.execute("Select university_name from university where t_u_id=" + self.t_u_id)
        university_name=self.cursor.fetchall()
        return university_name

    def get_university_location(self):
        self.cursor.execute("Select university_location from university where t_u_id=" + self.t_u_id)
        university_location=self.cursor.fetchall()
        return university_location

    def get_university_iso_certificate(self):
        self.cursor.execute("Select iso_certified from university where t_u_id=" + self.t_u_id)
        university_iso_certi=self.cursor.fetchall()
        return university_iso_certi

    def get_university_details(self):
        name = self.get_university_name()
        location = self.get_university_location()
        iso = self.get_university_iso_certificate()
        return name,location,iso
