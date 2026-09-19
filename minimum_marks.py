class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def lowest_marks(self):
        lowest = self.marks[0]

        for mark in self.marks:
            if mark < lowest:
                lowest = mark

        print("Lowest Marks =", lowest)

s1 = Student("Prathamesh", [80,90,90])
s1.lowest_marks()

s2 = Student("Devashish", [80,70,80])
s2.lowest_marks()

s3 = Student("Harsh", [80,70,90])
s3.lowest_marks()