import random
def getRandomnum():
    return random.randrange(1,101)
def givehint(number,guess):
    if (guess==number):
        return("You Right")
    else:
        return("Try next time")
def runguess():
    while True:
    	secretnumber=getRandomnum()
    	#print("The secret number is:",secretnumber)
    	userguess=int(input("Enter the number range from 1 to 101:"))
    	hint=givehint(secretnumber,userguess)
    	if hint == "You Right":
        		print("Your guess is the correct one")
    	else:
        		print(hint)
    	print("The secret number is:",secretnumber)
runguess()
