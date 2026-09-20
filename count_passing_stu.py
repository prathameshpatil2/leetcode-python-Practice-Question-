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

s3 = Student([30,70,35,60,90])
s3.count_pass()

s4 = Student([30,50,20,60])
s4.count_pass()

s5 = Student([80,60,20,30,40])
s5.count_pass()