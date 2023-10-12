#QUESTION 1
#Write a function to pPrint "hello_USERNAME!" USERNAME is the input of the function. The first line of the 
#code has been defined as below.

def hello_name(user_name):
    userName = user_name
    print("hello",userName,"!")
hello_name("swetha")


#QUESTION 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    for number in range(1, 101, 2):
        print(number)
#call the funstion to print odd numbers from 1 to 100 
first_odds() 



#QUESTION 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(nums):
    #check if the list is empty 
    if not nums:
          return None  #return none of the empty list
     
    #Initialize the maximum to the first element of the list
    maximum = nums[0]

    #Iterate through the list to find the maximum
    for num in nums:
          if num > maximum:
               maximum = num 
    
    return maximum 

#Example usage:
my_list = [3,7,1,9,4,2,6]
max_value = max_num_in_list(my_list)
print("The maximum number in the list is:", max_value)


#QUESTION 4
#Write a function to return if the given year is a leap year.
#A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
#The return should be boolean Type (true/false).

def is_leap_year(year):
    #leap year condtions:
    # 1. The year must be evenly divisible by 4.
    # 2. If It's divisible by 100, it must also be divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
       return True 
    else:
        return False 
    
#Example usage:
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
    #check if the list is empty or has only one element 
    if len (numbers) < 2:
        return True 

    #sort the list in ascending order 
    numbers.sort()

    #check if the numbers are consecutive
    for i in range(1, len(numbers)):
           if numbers[i] != numbers[i - 1] + 1:
                return False
           
    return True

#example usage 
my_list = [1, 2, 3, 4, 5]
result = is_consecutive(my_list)
print("Are the numbers consecutive?", result) 





