#Given a list of integers, find all the even numbers and store them in a new list

x = [25, 88, 29, 72, 67, 50, 99, 24, 31]

# iterating each number in list
for num in x:
# # checking condition
    if num % 2 == 0:
        print(num, end="  ")