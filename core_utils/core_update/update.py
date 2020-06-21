from Tools.scripts.treesync import raw_input


class Update:
    def __init__(self,cursor,db):
        self.cursor = cursor
        self.db=db

    def update_details(self,roll_no):

        try:
            student_name=raw_input("Update the student Name")
            # print student_name
            # print roll_no
            self.update_student_name(roll_no,"\""+student_name+"\"")
        except Exception as e:
            print (e)
        # print "heelo"
    def update_student_name(self,roll_no,student_name):
        print("Update student SET student_name = "+student_name+" "+"where roll_no= "+roll_no)
        self.cursor.execute('''Update student SET student_name = ? where roll_no= ?''',(student_name,roll_no))
        # print("Update student SET student_name = " + student_name + " " + "where roll_no= " + roll_no)
        self.db.commit()
        # '''UPDATE books SET price = ? WHERE id = ?''', (newPrice, book_id)

