t = 0
for k in range(5, 7, 1):
    print(k)
    t = t + 1
print(t)


def add_one(the_list):
  #  result = []
  #  for x in the_list:
  #      result.append(x + 1)
  #  return result

  #  for i in range(len(the_list)):
  #      the_list[i] = the_list[i] + 1
  #  return the_list

    for i in range(len(the_list)):
        the_list[i] = the_list[i] + 1


list = [1, 2, 3]
add_one(list)
print(list)
