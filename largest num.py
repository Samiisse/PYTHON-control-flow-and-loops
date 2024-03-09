#Implement a program that finds the largest number in a list
#x = numbers
def find_largest_number(x):
    maximum = max(x)
    return maximum

x = [68, 28, 99, 102, 67, 1087, 10000]
max_value = find_largest_number(x)
print(f"Maximum Value: {max_value}")
