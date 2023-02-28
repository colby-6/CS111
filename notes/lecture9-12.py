#summation is really just saying that something is a while loop 
#lambda expressions are written like name- NEW NAME - lambdax ....: x.x or something 
# ! LOOK AT LAMBDA EXPRESSIONS ON GOOGLE 
def tik(tok):
    def insta(gram):
        print(tok,gram)
    return insta
tik(tik(5)(print(6)))(print(7))