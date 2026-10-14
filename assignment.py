def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: 
# The numbers that are printed are 3 and 4. The function inspects all numbers 1, 2 and 3
#In this case add_one (2) prints 3 and add_one (3) prints 4 because we are adding one to each.

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer:
#Add_one returns 3 because we are giving one value to it. Return gives back a result to the program that called the function.
#print is what displays the result.
