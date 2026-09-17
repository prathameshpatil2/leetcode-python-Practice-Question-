class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        total = 0

        for mark in self.marks:
            total += mark

            average = total / len(self.marks)

            print(self.name)
            print("Average =", average)

s1 = Student("Prathamesh", [80,90,70])
s1.get_average()

s2 = Student("Devashish", [90,80,70])
s2.get_average()

s3 = Student("Ritesh", [70,60,70])
s3.get_average()

s4 = Student("Mayuresh", [80,80,70])
s4.get_average()

s5 =Student("Harsh", [80,70,80])
s5.get_average()