def deep_reverse(lst):
    """Get a list and return the reversal of this list

       Parameters
       ----------
       lst: a list, or a nested lists of integers

       Returns
       -------
       list: a reversal of the list, which can be a nested list or a normal list

    """
    # Base case: if the list if empty, return an empty list
    if len(lst) == 0:
        return lst
    else:
        if isinstance(lst[0], list):
            # Recursive case: deeply reverse the list order if the first element is a list
            return deep_reverse(lst[1:]) + [deep_reverse(lst[0])]
        else:
            # Recursive case: reverse the list order
            return deep_reverse(lst[1:]) + [lst[0]]


def multiply_coeff_and_add_exp(single_term, lst):
    """Multiply a single term with each term of the other polynomials by a formula of multiplying coefficients and adding exponents

       Parameters
       ----------
       single_term: a list, represent a single term of a polynomial having a format of [coefficient, exponent]
       lst: a list, represent a polynomial

       Returns
       -------
       list: a polynomial having a format of [coefficient, exponent]

    """
    result = []
    for term in lst:
        # Multiply the coefficients and add exponents
        result.append([single_term[0] * term[0], single_term[1] + term[1]])
    return result


def add_poly(poly1, poly2):
    """Add two polynomials having the same exponents and return the sum with their exponents in a descending order

       Parameters
       ----------
       poly1, poly2: two lists representing polynomials having a format of [coefficient, exponent]

       Returns
       -------
       list: a new polynomial, which is the sum of poly1 and poly2

    """
    result = {}
    for term in poly1 + poly2:
        coeff, exp = list(term)
        # Sum coefficients for same exponent
        if exp in result:
            result[exp] += coeff
        else:
            result[exp] = coeff
    # Sort by descending exponents and filter the zero coefficients
    return [[coeff, exp] for exp, coeff in sorted(result.items(), reverse=True) if coeff != 0]


def multiply_poly(lst1, lst2):
    """Get two nested lists representing two polynomials and return a nested list representing the multiplication of the given two polynomials

       Parameters
       ----------
       lst1, lst2: two nested lists in which each list has a format of [coefficient, exponent]

       Returns
       -------
       list: a nested list representing the multiplication of polynomials

    """
    # Base case: if either list is empty, return an empty list
    if lst1 == [] or lst2 == []:
        return []
    else:
        # Recursive case: multiply the first term of list 1 with list 2, and recurse for the rest
        return add_poly(multiply_coeff_and_add_exp(lst1[0], lst2), multiply_poly(lst1[1:], lst2))
