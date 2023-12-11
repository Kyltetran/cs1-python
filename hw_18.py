class CS1_grade:
    def __init__(self, first_name, last_name, quiz, programming_test, mid_term, final_exam, bonus=0):
        self.first_name = first_name
        self.last_name = last_name
        self.quiz = quiz
        self.programming_test = programming_test
        self.mid_term = mid_term
        self.final_exam = final_exam
        self.bonus = bonus
        assert first_name and last_name, "First name or last name cannot be empty"
        assert all(0 <= grade <= 100 for grade in
                   [quiz, programming_test, mid_term, final_exam, bonus]), "Grades must be between 0 and 100"

    def get_course_grade(self):
        grade = self.quiz * 0.2 + self.programming_test * 0.2 + \
            self.mid_term * 0.25 + self.final_exam * 0.35 + self.bonus
        if grade >= 90:
            return 'A'
        elif 80 <= grade < 90:
            return 'B'
        elif 70 <= grade < 80:
            return 'C'
        elif 60 <= grade < 70:
            return 'D'
        else:
            return 'F'
