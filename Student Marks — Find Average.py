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