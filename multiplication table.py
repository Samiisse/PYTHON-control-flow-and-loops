#Implement a program that prints the multiplication table of a given number

def multiplication_table(number):
    print(f"Multiplication Table for {number}: ")
    
    for i in range(1 , 11): #loop itarate from 1 to 10
        result = number * i
        print(f"{number} * {i} = {result}")

number = int(input("Enter a number for the multiplication table: "))
multiplication_table(number)
