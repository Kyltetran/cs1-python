class CS1_grade:
    def __init__(self, name, quiz, programming_test, mid_term, final_exam, bonus=0):
        self.name = name
        self.quiz = quiz
        self.programming_test = programming_test
        self.mid_term = mid_term
        self.final_exam = final_exam
        self.bonus = bonus
        assert self.quiz >= 0 and self.quiz <= 100


# student_1_grade = CS1_grade('quynh_tran', 700, 80, 97, 93)


# # Give a comment to clarify what are those figures
# cs1_dict = {'knoi_bui': [70, 80, 97, 73]}
