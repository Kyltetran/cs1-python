def list_sum(lst1, lst2):
    """Add elements from two lists at corresponding positions

       Parameters
       ----------
       lst1, lst2: two lists of integers having the same length

       Returns
       -------
       list: a new list where each element is the sum of elements from lst1 and lst2 at the same index

    """
    # Base case: if either list is empty, return an empty list
    if lst1 == [] or lst2 == []:
        return []
    else:
        # Recursive case: sum the first elements and recurse for the rest
        return [lst1[0] + lst2[0]] + list_sum(lst1[1:], lst2[1:])


def int_to_binary(n):
    """Convert an integer to its binary representation

       Parameters
       ----------
       n: a positive integer

       Returns
       -------
       str: the binary string representation of 'n'

    """
    # Base case: if the number is 0 or 1, return its string representation
    if n == 0 or n == 1:
        return str(n)
    else:
        # Recursive case: build the binary string from right to left
        return int_to_binary(n // 2) + str(n % 2)


def eval_continued_frac(lst):
    """Calculate the value of a continued fraction

       Parameters
       ----------
       lst: a list of integers

       Returns
       -------
       float: the evaluated value of the continued fraction

    """
    # Base case: if the list is empty, return 0
    if lst == []:
        return 0
    else:
        if len(lst) == 1:
            return lst[0]
        else:
            # Recursive case: apply the continued fraction formula
            return lst[0] + 1 / eval_continued_frac(lst[1:])
