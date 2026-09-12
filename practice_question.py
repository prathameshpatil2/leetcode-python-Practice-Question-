class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_total(self):
        total = 0

        for mark in self.marks:
            total += mark

        print(self.name)
        print("Total =", total)

s1 = Student("Prathamesh", [80,90,70])
s1.get_total()