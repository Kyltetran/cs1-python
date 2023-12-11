def check_email_address(mail):
    if not ' ' in mail and mail.count('@') == 1 and (mail[-4:] == '.com' or mail[-4:] == '.edu'):
        return 'Yes'
    else:
        return 'No'


class quiz_score:
    def __init__(self, score, cheating):
        if cheating:
            self.grade = 'NP'
        else:
            if score >= 70:
                self.grade = 'P'
            else:
                self.grade = 'NP'

    def print_grade(self):
        print(self.grade)


test_email_1 = 'sample@fulbight.edu'
print(check_email_address(test_email_1))


class number:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate(self):
        self.a = self.a * self.b
        self.b = self.b - self.a
        self.c = self.a + self.b
        print(self.a)
        print(self.b)
        print(self.c)


num_1 = number(1, 2, 3)
print(num_1.calculate())
