#QUESTION 1
#Write a function to pPrint "hello_USERNAME!" USERNAME is the input of the function. The first line of the 
#code has been defined as below.

def hello_name(user_name):
    USERNAME = user_name
    print("hello_",USERNAME,"!")

    
#QUESTION 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
for number in range(1, 101, 2):
print(number)

# Call the function to print the odd numbers from 1 to 100
first_odds()

#QUESTION 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def is_consecutive(numbers):
# Check if the list is empty or has only one element
if len(numbers) < 2:
return True

# Sort the list in ascending order
numbers.sort()

# Check if the numbers are consecutive
for i in range(1, len(numbers)):
if numbers[i] != numbers[i - 1] + 1:
return False

return True

# Example usage:
my_list = [1, 2, 3, 4, 5]
result = is_consecutive(my_list)
print("Are the numbers consecutive?", result)

#QUESTION 4
#Write a function to return if the given year is a leap year.
#A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
#The return should be boolean Type (true/false).

def is_leap_year(year):
# Leap year conditions:
# 1. The year must be evenly divisible by 4.
# 2. If it's divisible by 100, it must also be divisible by 400.

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
return True
else:
return False

# Example usage:
year = 2024
if is_leap_year(year):
print(f"{year} is a leap year.")
else:
print(f"{year} is not a leap year.")

#QUESTION 5
#Write a function to check to see if all numbers in list are consecutive numbers.
#For example, [2,3,4,5,6,7] are consecutive numbers,
#but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(numbers):
# Check if the list is empty or has only one element
if len(numbers) < 2:
return True

# Sort the list in ascending order
numbers.sort()

# Check if the numbers are consecutive
for i in range(1, len(numbers)):
if numbers[i] != numbers[i - 1] + 1:
return False

return True

# Example usage:
my_list = [1, 2, 3, 4, 5]
result = is_consecutive(my_list)
print("Are the numbers consecutive?", result)





