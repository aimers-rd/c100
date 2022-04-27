class Student(object):
    def __init__(self,name,age,gender,level,grades=None):
        self.name=name
        self.age=age
        self.gender=gender
        self.level=level
        self.grades=grades or {}
    def setGrade(self, course, grade):
        self.grades[course] = grade
    def getGrade(self, course):
        return self.grades[course]
    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)

john=Student("john",12,"male",6,{"math":3.3})
riya=Student("riya",12,"female",6,{"math":3.5})
print(riya.getGPA())

