def approximate_pi(n):
    '''Calculate the approximation of pi obtained using the Leibniz formula

       Parameters
       ----------
       n : an integer, which is the number of terms

       Returns
       -------
       a float : the approximation of pi after considering 'n' terms, rounded to 12 decimal places

    '''

    # Set the approximation of pi to zero
    pi_approximation = 0

    # Iterate n times to refine the approximation of pi
    for i in range(n):

        # For each term, the result will be calculated as below
        pi_approximation += 4 * ((-1)**i / (2*i + 1))

    # Return the approximation of pi rounded to 12 decimal places
    return round(pi_approximation, 12)


def to_pig_latin(word):
    '''Transform a single word from English to Pig Latin

       Parameters
       ----------
       word: a single string

       Returns
       -------
       the transformation of the string

    '''

    # Define the vowel tuple
    vowel = ('a', 'e', 'i', 'o', 'u')

    # Check if the first letter in a string is a vowel or not
    if word[0] in vowel:

        # If so, it will append 'way' at the end
        return word + 'way'

    # Loop through the word's indexes to find the position of the first vowel
    for i, letter in enumerate(word):

        # Check if the first vowel is found
        if letter in vowel:

            # If so, everything after the vowel comes first, followed by the consonant cluster and 'ay'
            return word[i:] + word[:i] + 'ay'


print(to_pig_latin("duck"))
