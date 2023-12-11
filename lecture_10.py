def remove_redundant_space(x):
    y = x.replace("   ", " ")
    z = y.replace("  ", "")
    print(z)
    t = z.replace(" ", "")
    return t

def get_name(fuv_email):
    words = fuv_email.split(".")
    return [words[0], words[1]]

result = get_name("first.last.231234@student.fulbright.edu.vn")
print(type(result))
print(result)
