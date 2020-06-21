import sqlite3
db=sqlite3.connect(':memory:')
db=sqlite3.connect('C:\\Users\\Aman\\PycharmProjects\\UnversityManagementSystem\\information')

cursor=db.cursor()
cursor.execute('''CREATE TABLE student(student_id TEXT PRIMARY KEY, roll_no INTEGER, student_name TEXT, student_branch TEXT, student_gender TEXT, s_c_id TEXT, s_u_id TEXT)''')

student_id=["15DCHCE41", "15DCHCE48", "16DCHCE902","16KUPT002","17KUPT313","15IPSM820","15IPSM840","16IPSM941","18GJUMI416","17MDUBM201","18AMCR004"]
roll_no=["31241", "31248", "31281","91002","91313","10820","10840","11941","00416","12201","18004"]
student_name=["Saurabh Narang", "Tarun Kumar", "Lalit Saini","Annie Jain","Sonu Sharma","Seema Vohra","Ronak Verma","Deepak Gupta","Sandeep Sharma","Ashish Sajwan","Avinash Kumar"]
student_branch=["CSE", "CSE", "CSE","ECE","CE","EE","EE","CSE","ME","AE","IT"]
student_gender=["MALE", "MALE", "MALE","Female","MALE","FEMALE","MALE","MALE","MALE","MALE","MALE"]
s_c_id=["HCE31241", "HCE31248", "HCE31281","PT002","PT313","SM820","SM840","SM941","MI416","BM201","CR004"]
s_u_id=["DC1041", "DC1048", "DC902","KU91002","KU91313","IP10820","IP10840","IP11941","GJU00416","MDU12201","AM18004"]


for i in range (len(student_id)):
    print(roll_no[i])
    print(student_name[i])
    print(student_branch[i])
    print(student_gender[i])
    print(s_c_id[i])
    print(s_u_id[i])

    cursor.execute('''INSERT into student(student_id, roll_no, student_name, student_branch, student_gender, s_c_id, s_u_id) VALUES(?,?,?,?,?,?,?)''',(student_id[i], roll_no[i], student_name[i], student_branch[i], student_gender[i], s_c_id[i], s_u_id[i]))


cursor.execute('''CREATE TABLE teacher(teacher_id TEXT, teacher_name TEXT, teacher_department TEXT, student_roll_no TEXT, t_u_id TEXT, t_c_id TEXT)''')

teacher_id=["07DCHCE01", "04DCHCE02", "09DCHCE03","03KUPT11","02KUPT70","16IPSM97","16IPSM97","19IPSM50","17GJUMI77","23MDUBM69","14AMCR14"]
teacher_name=["Preeti Aneja", "Sonia Juneja", "Ashu Bansal","Sandeep Jain","Rohit Sharma","Suman Arora","Suman Arora","Nitin Jain","Puneet Sharma","Deepanshu Sharma","Tarun Kumar"]
teacher_department=["CSE", "IT", "CSE","ECE","CE","EE","EE","CSE","ME","AE","IT"]
student_roll_no=["31241", "61002", "31248","91002","91313","10820","10840","11941","00416","12201","18004"]
t_u_id=["DC0701", "DC0402", "DC0903","KU0301","KU0270","IP1697","IP1697","IP1950","GJU1777","MDU2369","AM1414"]
t_c_id=["HCE0107", "HCE0204", "HCE0309","PT1103","PT7002","SM9716","SM9716","SM5019","MI7717","BM6923","CR1414"]

for i in range (len(teacher_id)):
    print(teacher_name[i])
    print(teacher_department[i])
    print(student_roll_no[i])
    print(t_u_id[i])
    print(t_c_id[i])

    cursor.execute('''INSERT into teacher(teacher_id, teacher_name, teacher_department, student_roll_no, t_u_id, t_c_id) VALUES(?,?,?,?,?,?)''',(teacher_id,teacher_name[i], teacher_department[i], student_roll_no[i], t_u_id[i], t_c_id[i]))


cursor.execute('''CREATE TABLE college(college_id TEXT, college_name TEXT, college_location TEXT, c_u_id TEXT, s_c_id TEXT, t_c_id TEXT)''')

college_id=["007","007","007","001","001","005","005","005","009","011","010"]
college_name=["HCE","HCE","HCE","PIET","PIET","SM","SM","SM","MI","BM","CR"]
college_location=["Sonipat","Sonipat","Sonipat","Panipat","Panipat","Delhi","Delhi","Delhi","Hisar","Sonipat","Delhi"]
c_u_id=["02007","02007","02007","04001","04001","06005","06005","06005","03009","05011","07010"]
s_c_id=["HCE31241","HCE31248","HCE31281","PT002","PT313","SM820","SM840","SM941","MI416","BM201","CR004"]
t_c_id=["HCE0107","HCE0204","HCE0309","PT1103","PT7002","SM9716","SM9716","SM5019","MI7717","BM6923","CR1414"]

for i in range (len(college_id)):
    print(college_name[i])
    print(college_location[i])
    print(c_u_id[i])
    print(s_c_id[i])
    print(t_c_id[i])

    cursor.execute('''INSERT into college(college_id, college_name, college_location, c_u_id, s_c_id,t_c_id) VALUES(?,?,?,?,?,?)''',(college_id[i], college_name[i], college_location[i], c_u_id[i], s_c_id[i], t_c_id[i]))

cursor.execute('''CREATE TABLE university(university_id TEXT, university_name TEXT, university_location TEXT, iso_certified TEXT, c_u_id TEXT, t_u_id TEXT, s_u_id TEXT)''')

university_id=["02","02","02","04","04","06","06","06","03","05","07"]
university_name=["DCRUST","DCRUST","DCRUST","KU","KU","IP","IP","IP","GJU","MDU","Amity"]
university_location=["MURTHAL","Murthal","Murthal","Kurushetra","Kurushetra","DELHI","Delhi","Delhi","Hisar","Rohtak","Noida"]
iso_certified=["YES","YES","YES","YES","YES","YES","YES","YES","YES","YES","NO"]
c_u_id=["02007","02007","02007","04001","04001","06005","06005","06005","03009","05011","07010"]
t_u_id=["DC0701","DC0402","DC0903","KU0301","KU0270","IP1697","IP1697","IP1950","GJU1777","MDU2369","CR1414"]
s_u_id=["DC1041","DC1048","DC902","KU91002","KU91313","IP10820","IP10840","IP11941","GJU00416","MDU12201","AM18004"]

for i in range (len(university_id)):
    print(university_name[i])
    print(university_location[i])
    print(iso_certified[i])
    print(c_u_id[i])
    print(t_u_id[i])
    print(s_u_id[i])

    cursor.execute('''INSERT into university(university_id, university_name, university_location, iso_certified ,c_u_id, t_u_id, s_u_id) VALUES(?,?,?,?,?,?,?)''',(university_id[i], university_name[i], university_location[i],iso_certified[i], c_u_id[i], t_u_id[i], s_u_id[i]))

db.commit()
db.close()