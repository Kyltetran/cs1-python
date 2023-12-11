def reverse_words(string):
    '''Reverse the order of words in the given string and modify the casing of the first and last words in the resulting sentence

        Parameters
        ----------
        string : string, the input sentence

        Returns
        -------
        The modified sentence after reversing and adjusting casing

    '''
    # Split the input string into individual words
    string = string.split()

    # Check if the string is empty or has only one word
    if len(string) <= 1:
        # If so, capitalize the entire string and return
        return ' '.join(string).capitalize()
    else:
        # If not, reverse the order of the words in the list
        string = string[::-1]

        # Capitalize the first letter of the first word in the reversed list
        string[0] = string[0][0].upper() + string[0][1:]

        # Convert the first letter of the last word in the reversed list to lowercase
        string[-1] = string[-1][0].lower() + string[-1][1:]

        # Join the modified list of words back into a single string and return
        return ' '.join(string)
