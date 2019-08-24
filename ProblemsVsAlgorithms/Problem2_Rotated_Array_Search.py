
# coding: utf-8

# In[1]:

def search (input_list, l, h, number): 
    if l > h: 
        return -1
      
    midpoint = (l + h) // 2
    if input_list[midpoint] == number: 
        return midpoint 
    
    if input_list[l] <= input_list[midpoint]:  
        if number >= input_list[l] and number <= input_list[midpoint]: 
            return search(input_list, l, midpoint-1, number) 
        return search(input_list, midpoint+1, h, number) 

    if number >= input_list[midpoint] and number <= input_list[h]: 
        return search(input_list, midpoint+1, h, number) 
    return search(input_list, l, midpoint-1, number) 

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    l = 0
    h = len(input_list)-1
    if linear_search(input_list, number) == search(input_list, l, h, number):
        #print ((linear_search(input_list,number)),(rotated_array_search(input_list, l, h, number)))
        print("Pass")
    else:
        print ((linear_search(input_list,number)),(search(input_list, l, h, number)))
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

