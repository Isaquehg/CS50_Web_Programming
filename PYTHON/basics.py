#importing a function from other file
#if we've used IMPORT FUNCTIONS without square, we'd use functions.square()
from functions import square

#converting types
n = int(input("Enter a number: "))
if(n > 0):
    print("n is positive")
elif(n < 0):
    print("n is negative")
else:
    print("n is equal to zero")

#accessing dicts
languages = {"Python": 1, "C++": 2, "JS": 3}
languages["C++"] = 0
print(languages["C++"])

#using functions from another file
for i in range(10):
    print(f"The square of {i} is {square(i)}")