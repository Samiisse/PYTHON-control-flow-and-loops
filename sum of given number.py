#Calculate the sum of digits of a given number

def sum_of_digits(number):
    # Convert the number to a string to iterate over its digits
    num_str = str(number)
    # Initialize the sum
    total = 0
    # Iterate over each character in the string
    for digit_char in num_str:
        # Convert the character back to integer and add it to the sum
        total += int(digit_char)
    return total

# Example usage:
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of digits of {number} is: {result}")
