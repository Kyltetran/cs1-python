def get_simon_says(instructions):
    '''Return a list of obeyed instructions issued by Simon

       Parameters
       ----------
       instructions: a list of strings containing instructions

       Returns
       -------
       a list of obeyed instructions starting with 'Simon says'

    '''

    # A list to store obeyed instructions
    obeyed_instructions = []

    # Iterate every instruction in the provided list
    for instruction in instructions:

        # Check if each instruction starts with 'Simon says'
        if instruction.startswith('Simon says'):

            # If so, the list obeyed_instructions append the part of all coming after 'Simon says'
            obeyed_instructions.append(instruction[11:])

    return obeyed_instructions


def get_most_frequent_letter(str):
    '''Return a letter that appears in a provided string most often

       Parameters
       ----------
       str: a string

       Returns
       -------
       the most frequent letter in the provided string

    '''

    # A dictionary to store the frequency of each letter in a string
    letter_frequency = {}

    # Iterate each letter in the provided string
    for letter in str:

        # Ensure the letter is alphabetic
        if letter.isalpha():

            # If the letter is already in the dictionary, increase the count
            if letter in letter_frequency:
                letter_frequency[letter] += 1

            # If the letter is NOT in the dictionary, add the letter with a count of 1
            else:
                letter_frequency[letter] = 1

    # Initialize variables to track the highest frequency seen so far and the corresponding letter
    max_frequency = 0
    most_frequent_letter = None

    # Iterate over letters and frequencies in the dictionary
    for letter, frequency in letter_frequency.items():

        # If the frequency of the letter is greater than the highest seen so far
        if frequency > max_frequency:

            # Update the highest frequency seen so far and the corresponding letter
            max_frequency = frequency
            most_frequent_letter = letter

    return most_frequent_letter
