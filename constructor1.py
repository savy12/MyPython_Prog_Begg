class stu:
    def __init__(self,name):
        self.name = name
        self.attend =0
        self.marks = []
        print("name {} ".format(name))
    def addmarks(self,ma):
        self.marks.append(ma)
    def attenddays(self):
        self.attend += 1
    def getavg(self):
        return sum(self.marks)/len(self.marks)
    
