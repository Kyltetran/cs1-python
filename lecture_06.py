
class TA:
    def __init__(self, input_first_name, input_last_name, input_student_id, input_course, input_homework):
        self.first_name = input_first_name
        self.last_name = input_last_name
        self.student_id = input_student_id
        self.course = input_course
        self.homework = input_homework

    def get_FUV_email(self):
        return self.first_name + '.' + self.last_name + '.' + self.student_id + '@student.fulbright.edu.vn'

    def get_message(self):
        return 'Hi ' + self.first_name + ', Please help me check the ' + self.homework + ' of ' + self.course + ' Best, Linh'


ta_1 = TA('Phuong', 'Pham', '201111', 'CS302', 'homework 4')
ta_1_email = ta_1.get_FUV_email()
ta_1_message = ta_1.get_message()
print(ta_1_email)
print(ta_1_message)

ta_2 = TA('Khoi', 'Bui', '201111', 'CS302', 'homework 4')
ta_2_email = ta_2.get_FUV_email()
ta_2_message = ta_2.get_message()
print(ta_2_email)
print(ta_2_message)
