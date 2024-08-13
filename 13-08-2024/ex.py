class Student:
    def __init__(self):
        self.scores = []
        
    @property
    def name(self):
        return self.n

    @name.setter
    def name(self,n):
        self.n = n

    @property
    def roll(self):
        return self.r

    @roll.setter
    def roll(self,r):
        self.r = r

    def set_score(self, subject, marks):
        self.scores.append((subject, marks))

    def get_average(self):
        total_score = sum(marks for subject, marks in self.scores)
        return total_score // len(self.scores) if self.scores else 0

if __name__ == "__main__":
    s1 = Student()
    s1.name = "Deepak tala"
    s1.roll = 21
    ch = input("Enter n to quit and s to enter your subject names and their marks: ")
    if ch == 's':
        while True:
            sub = input("Enter name of subject or enter exit to exit: ")
            if sub == "exit":
                break
            mark = float(input("Enter marks of this subject: "))
            s1.set_score(sub, mark)
        print("Your average score is", s1.get_average())

