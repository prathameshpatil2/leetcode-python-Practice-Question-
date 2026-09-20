class Student:

    def __init__(self,marks):
        self.marks = marks

    def count_pass(self):
        count = 0

        for mark in self.marks:
            if mark >= 40:
                count += 1

        print("Passing Student =",count)

        