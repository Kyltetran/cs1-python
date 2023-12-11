def get_simon_says(instructions):
    result = []
    for i in range(len(instructions)):
        if instructions[i].startswith('Simon says'):
            result.append(instructions[i][11:])
    return result


print(get_simon_says(
    ['Simon says smile', 'Clap your hands', 'Simon says jump', 'Nod your head']))
print(get_simon_says(
    ['simon says wave', 'Simon say jump', 'Simon says twist and shout']))
print(get_simon_says(
    ['simon says wave', 'simon says jump', 'simon says clap']))
print(get_simon_says(['Jump', 'Simon says wave']))


def get_most_frequent_letter(str):
    letter_frequency = {}
    for letter in str:
        if letter.isalpha():
            if letter in letter_frequency:
                letter_frequency[letter] += 1
            else:
                letter_frequency[letter] = 1
    sorted_frequence = sorted(letter_frequency.items(), key=lambda x: x[1])
    return sorted_frequence[-1][0]
