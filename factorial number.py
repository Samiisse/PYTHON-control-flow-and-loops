#factorial of a given number

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial (x-1)

number = int(input("Enter a number to generarate its factorial: "))
print(f"The factorial {number} is: {factorial(number)}")