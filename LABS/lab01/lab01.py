# Lab 01: Variables, Functions, and Control
# Submit this file.

# Required Questions

# Q3: Falling Factorial
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k <= 0:
        return 1

    total = 1

    while k > 0:
        total = total * n

        n, k = n - 1, k - 1

    return total


# Q4: Sum Digits
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    digits = []
    y = str(y)
    
    for number in y:
        digits.append(int(number))
        '''
            for digit in digits:
        final_sum = 0
        final_sum = final_sum + digit
        '''
    final_sum = sum(digits)

    return (final_sum)




# Extra Practice

# Q6: Double Eights
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
