# Research about the OOPs concepts
#
# Task 1 - Create a Class PyATB , 5 Attributes, 3 Functions/Methods
#
# Use PC - to set the value of the attributes
#
# create a Print student information method/function
#
# 3 studetns objects
#
# PyATB().print_student_infomation()


class PYATB:

    def __init__(self, id,name,branch,age,batch):
        self.id = id
        self.name = name
        self.branch = branch
        self.age = age
        self.batch = batch

    def print_Student_info(self):
        print("Id of student is",self.id)
        print("Name of the student is",self.name)
        print("Branch of the student is",self.branch)
        print("Age of the student is",self.age)
        print("Batch of the student is",self.batch)




    # def id(self):
    #     print("Id of student is ",self.id)
    #
    # def branch(self):
    #     print("Branch of student is",self.branch)
    #
    # def age(self):
    #     print("age is", self.age)

Student_1 = PYATB(1,"shubham","MCA",22,4)
Student_2 =PYATB(2,"Amit","MBA",21,4)
Student_3 =PYATB(3,"Sumit","MCA",20,4)

Student_1.print_Student_info()
Student_2.print_Student_info()
Student_3.print_Student_info()
