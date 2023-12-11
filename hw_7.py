class Student:
    def __init__(self, input_first_name, input_last_name, input_student_id):
        self.first_name = input_first_name
        self.last_name = input_last_name

        if isinstance(input_student_id, (str, int)):
            self.student_id = str(input_student_id)
        else:
            raise ValueError(
                "Student ID should be either a string or an integer.")

    def get_FUV_email(self):
        domain = '@student.fulbright.edu.vn'
        if self.student_id.startswith(('18', '19')):
            domain = '@alumni.fulbright.edu.vn'
        return self.first_name + '.' + self.last_name + '.' + self.student_id + domain

    def get_letter_grade(self, percentage_grade):
        if percentage_grade >= 94:
            return 'A'
        elif percentage_grade >= 90:
            return 'A-'
        elif percentage_grade >= 87:
            return 'B+'
        elif percentage_grade >= 83:
            return 'B'
        elif percentage_grade >= 80:
            return 'B-'
        elif percentage_grade >= 77:
            return 'C+'
        elif percentage_grade >= 73:
            return 'C'
        elif percentage_grade >= 70:
            return 'C-'
        elif percentage_grade >= 67:
            return 'D+'
        elif percentage_grade >= 60:
            return 'D'
        else:
            return 'F'
