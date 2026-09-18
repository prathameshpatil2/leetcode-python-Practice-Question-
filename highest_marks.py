class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def highest_marks(self):
        highest = self.marks[0]

        for mark in self.marks:
            if mark > highest:
                highest = mark

        print("Highest Marks =", highest)

s1 = Student("Prathamesh", [90,80,95])
s1.highest_marks()

s2 = Student("Devashish", [80,90,80])
s2.highest_marks()