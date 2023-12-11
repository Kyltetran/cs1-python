class fuv_course:
    def __init__(self, code, title, description=''):
        self.code = code
        self.title = title
        self.description = description
        assert type(code) is str and type(title) is str
        assert len(code) > 0 and len(title) > 0

    def get_info(self):
        return self.code + '-' + self.title + self.description


class FUV_CS_course(fuv_course):
    def __init__(self, category, code, title, description):
        super().__init__(code, title, description)
        self.category = category

    def get_info(self):
        info = self.code + '-' + self.title \
            + '(' + self.category + ')'
        if len(self.description) > 0:
            info = info + ':' + self.description
        return info


class fuv_course:
    def __init__(self, code, title, description='', grade=None, letter_grade=None):
        self.code = code
        self.title = title
        self.description = description
        self.grade = grade
        self.letter_grade = letter_grade

        assert type(code) is str and type(title) is str
        assert len(code) > 0 and len(title) > 0
        assert grade is None or (isinstance(
            grade, float) or isinstance(grade, int))
        assert letter_grade is None or isinstance(letter_grade, str)

    def get_info(self):
        info = self.code + '-' + self.title
        if self.description:
            info += ': ' + self.description
        if self.grade is not None and self.letter_grade is not None:
            info += ' - Grade: ' + str(self.grade) + \
                ', Letter Grade: ' + self.letter_grade
        return info


calculus_course = fuv_course("MATH101", "Calculus", '', 3.2, "B")
cs1_course = fuv_course("CS101", "CS1", '', 3.9, "A")
cs2_course = fuv_course("CS102", "CS2", '', 3.6, "A-")

print(calculus_course.get_info())
print(cs1_course.get_info())
print(cs2_course.get_info())
