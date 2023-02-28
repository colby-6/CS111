
def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m 
    return m + multiply(m, n-1)
    
print(multiply(5,3))


isprime()