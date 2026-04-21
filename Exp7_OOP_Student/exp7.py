class student:
    def get_student(self):
        self.student=input("enter student name:")
        self.usn=input("enter usn:")

class marks(student):
    def get_marks(self):
        self.marks1=int(input("enter marks of subject 1:"))
        self.marks2=int(input("enter marks of subject 2:"))
        self.marks3=int(input("enter marks of subject 3:"))
        self.marks4=int(input("enter marks of subject 4:"))
        self.marks5=int(input("enter marks of subject 5:"))

    def calculate(self):
        print("student:",self.student)
        print("total marks:",self.marks1+self.marks2+self.marks3+self.marks4+self.marks5)

obj=marks()
obj.get_student()
obj.get_marks()
obj.calculate()

