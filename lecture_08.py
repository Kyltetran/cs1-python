def is_advanced(course_code):
  print(course_code)
  if course_code[-3] == '3':
    return 'Yes'
  else:
    return 'No'
  
def is_CS101_taken(course_list):
  print(course_list)
  if ('CS101' in course_list):
    return 'Yes'
  else:
    return 'No'
  
def is_CS_minor_fulfilled(course_list):
  print(course_list)
  if ('MATH202' in course_list or 'MATH205' in course_list) \
    and ('CS101' or 'CS102' or 'CS103' in course_list) \
    and ('CS201' in course_list) \
    and ('CS202' or 'CS302') \
    and course_list.count('CS2') >= 2 \
    and course_list.count('CS3') >= 2:
    return 'Yes'
  else:
    return 'No'
  
def get_FUV_email(first_name, last_name, student_ID):
  return first_name.lower() + '.' \
      + last_name.lower() + '.' \
      + student_ID \
      + '@student.fulbright.edu.vn'


  
      

print(is_advanced('CS101'))
print(is_advanced('CORE_101'))
print(is_advanced('CS302'))
print(is_advanced('ENG201'))
print(is_advanced('ECON303'))
print(is_advanced('ART303'))

print(is_CS101_taken('CS101, CORE_101, CS302, ENG201'))
print(is_CS101_taken('CS102, CORE_101, CS302, ENG201'))

