def mystery_1(filename):
    in_file = open(filename, 'r')
    text = in_file.read()
    in_file.close()
    print(text)
    return len(text)


def mystery_2(filename):
    in_file = open(filename, 'r')
    text = in_file.read()
    in_file.close()
    return "foo" in text


def mystery_3(filename):
    in_file = open(filename, 'r')
    out_file = open('output.txt', 'w')
    for line in in_file:
        words = line.split()
        if len(words) > 10:
            out_file.write(line + "\n")
    in_file.close()
    out_file.close()
