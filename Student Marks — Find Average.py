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


s2 = Student("Devashish", [80,90,60])
s2.get_average()

s3 = Student("Ritesh", [60,70,80])
s3.get_average()

s4 = Student("Mayuresh", [80,80,80])
s4.get_average()

s5 = Student("Harsh", [90,80,90])
s5.get_average()

s6 = Student("Anurag", [70,70,70])
s6.get_average()

s7 = Student("Sujeet", [70,60,60])
s7.get_average()

s8 = Student("Dhanraj", [60,50,40])
s8.get_average()

s9 = Student("Ranjeet", [70,80,77])
s9.get_average()