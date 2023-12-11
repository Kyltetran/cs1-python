class quiz_score:
    def __init__(self, score, cheating):
        if cheating:
            self.grade = "NP"
        else:
            if score >= 80:
                self.grade = "P"
            else:
                self.grade = "NP"

    def print_grade(self):
        print(self.grade)


q1 = quiz_score(75, True)
q1.print_grade()


class Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        self.a = self.a * self.b
        self.b = self.b - self.a
        print(self.a)
        print(self.b)


case_1 = Number(1, 2)
case_1.calculate()
