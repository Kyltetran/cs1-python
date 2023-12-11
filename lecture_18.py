class Course_grade:
    def __init__(self, name, quiz, programming_test, mid_term, final_exam, pass_non_pass):
        self.name = name
        self.quiz = quiz
        self.programming_test = programming_test
        self.mid_term = mid_term
        self.final_exam = final_exam
        self.pass_non_pass = pass_non_pass
        assert self.quiz >= 0 and self.quiz <= 100
        assert type(pass_non_pass) == bool

    def calculate_final_grade(self):
        if self.pass_non_pass:
            return 'P'
        else:
            return 'A'


class FUV_student:
    def __init__(self, first_name, last_name, student_ID, major='', advisor='', courses=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.student_ID = student_ID
        self.major = major
        self.advisor = advisor
        self.courses = courses


sample_student = FUV_student('first', 'last', 202020, 'CS', 'Prof.ABC',
                             [Course_grade('CS1', 90, 80, 90, 80, True),
                              Course_grade('SI', 90, 80, 90, 80, True),
                              Course_grade('GH', 90, 80, 90, 80, False),
                              Course_grade('DH', 90, 80, 90, 80, False)])

sample_student.calculate_final_grade()
