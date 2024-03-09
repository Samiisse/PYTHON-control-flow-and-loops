#check if a num is positive, negative or zero
#if else function

def positive_negative_zero(num):
    if num > 0:
        print("this number is positive")
    elif num < 0:
        print("this is a negative number")
    else:
        print("this number is zero")

num = float(input("Enter a number: "))
positive_negative_zero(num)