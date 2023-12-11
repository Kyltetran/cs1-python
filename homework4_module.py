def get_FUV_email(first_name, last_name, student_ID):
    return first_name + '.' \
        + last_name + '.' \
        + student_ID + \
        + '@student.fulbright.edu.vn'


def initial_deposit(A):
    return A / (1 + 0.085 / 4) ** (4 * 45)
