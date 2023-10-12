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