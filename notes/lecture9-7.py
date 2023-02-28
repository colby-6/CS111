# return statements are neccessary or your funciton will return none and not what you wrote
#side effects are when we call a function besudes just returning a value
# functional programming is all about not trying to have side effects, this is called a PURE function. print is a nonpure function because it has a side effect
#print(print(1), print(2))
#! learn more about doctests in pyton 


def divide_exact(n, d):
    quotient = n // d
    remainder = n % d
    return quotient, remainder

q, r = divide_exact(618, 10)
print(f'Your quotient is {q} and the remainer is {r}')