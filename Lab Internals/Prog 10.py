class Student:
    def __init__(self, name="", usn="", score=[0,0,0,0]):
        self.name = name
        self.usn = usn
        self.score = score

    def getMarks(self):
        self.name = input("Enter student Name: ")
        self.usn = input("Enter student USN: ")
        self.score[0] = int(input("Enter marks in Subject 1: "))
        self.score[1] = int(input("Enter marks in Subject 2: "))
        self.score[2] = int(input("Enter marks in Subject 3: "))
        self.score[3] = self.score[0] + self.score[1] + self.score[2]

    def display(self):
        percentage = self.score[3] / 3
        border = "=" * 81
        print(border)
        print("SCORE CARD DETAILS".center(81))
        print(border)
        print("%15s" % ("NAME"), "%12s" % ("USN"), "%8s" % "MARKs1", "%8s" % "MARKS2", "%8s" % "MARKS3","%8s" % "TOTAL", "%12s" % "PERCENTAGE")
        print(border)
        print("%15s" % self.name, "%12s" % self.usn, "%8d" % self.score[0], "%8d" % self.score[1],"%8d" % self.score[2], "%8d" % self.score[3], "%12.2f" % percentage)
        print(border)
s1 = Student()
s1.getMarks()
s1.display()


s2 = Student()
s2.getMarks()
s2.display()