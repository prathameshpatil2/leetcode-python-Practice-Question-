class Student:

    def __init__(self,marks):
        self.marks = marks

    def count_pass(self):
        count = 0

        for mark in self.marks:
            if mark >= 40:
                count += 1

        print("Passing Student =",count)

s1 = Student([80,90,80,30,35])
s1.count_pass()

s2 = Student([20,30,40,50,60,70])
s2.count_pass()