def check_string_type(string):
    '''Check the type of the string whether it is symmetrical or palindrome or both
       Parameter: any string

       Return one of the four categories: 
        - Symmetrical and palindrome
        - Symmetrical but not palindrome
        - Not symmetrical but palindrome
        - Not symmetrical and not palindrome

       How function goes:
        - If the length of the string is even, it splits the string into two equal halves.
        - If the length of the string is odd, it splits the string into two halves such that the middle character is excluded.
        - If the two halves obtained from the split are equal, the string is symmetrical.
        - If the string is the same when reversed, the string is palindrome.
        - Based on the above checks, the function classifies the string into one of the four categories.
    '''
    if len(string) % 2 == 0:
        first_half = string[:len(string) // 2]
        second_half = string[len(string) // 2:]
    else:
        first_half = string[:len(string) // 2]
        second_half = string[len(string) // 2 + 1:]

    is_symmetrical = (first_half == second_half)
    is_palindrome = (string == string[::-1])

    if is_symmetrical and is_palindrome:
        return 'Symmetrical and palindrome'
    elif is_symmetrical and not is_palindrome:
        return 'Symmetrical but not palindrome'
    elif not is_symmetrical and is_palindrome:
        return 'Not symmetrical but palindrome'
    else:
        return 'Not symmetrical and not palindrome'


def is_speakable(name):
    '''Check if the given name can be pronounced by the character Pikachu or not
       Parameter: name as a string

       Return: 
       - Yes if the name can be pronounced by Pikachu
       - No if the name cannot be pronounced by Pikachu

       How function goes:
       - The function examines the start of the name to see if it begins with 'pi', 'ka', 'chu' or a space.
       - If the start of the name matches one of those, the syllable will be removed, and the string becomes shorter.
       - It will get shorter and shorter until it is empty, then return 'Yes'.
       - If it is not an empty string because there is any unspeakable syllable remained, then return 'No'.
    '''
    if not name:
        return 'Yes'
    if name.startswith('pi'):
        return is_speakable(name[2:])
    if name.startswith('ka'):
        return is_speakable(name[2:])
    if name.startswith('chu'):
        return is_speakable(name[3:])
    if name.startswith(' '):
        return is_speakable(name[1:])
    return 'No'
