class fuv_student:
    def __init__(self, name):
        self.name = name

    def get_greeting(self):
        return 'Hi' + self.name


class FUV_student_grade:
    def __init__(self):
        self.grade = {}

    def add_course_grade(self, course_code, course_grade):
        self.grade[course_code] = course_grade

    course_grade_dict = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
                         'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0}

    def get_GPA(self):
        total_point = 0
        count = 0
        for grade in self.grade.values():
            if grade in self.course_grade_dict.keys():
                total_point += self.course_grade_dict[grade]
                count += 1
                result = round((total_point / count), 2)
        return result

    def get_CS_GPA(self):
        total_point = 0
        count = 0
        for course, grade in self.grade.items():
            if course[:2] == 'CS' and \
               grade in self.course_grade_dict.keys():
                total_point += self.course_grade_dict[grade]
                count += 1
                result = round((total_point / count), 2)
        return result
