class TA:
  def __init__(self, input_first_name, input_last_name, input_student_id, input_course):
    self.first_name = input_first_name
    self.last_name = input_last_name
    self.student_id = input_student_id
    self.course = input_course

  def get_FUV_email(self):
    return self.first_name + '.' + self.last_name + '.' + self.student_id + '@student.fulbright.edu.vn'