
# coding: utf-8

# In[1]:

def sort_012(inputlist): 
    listsize = len(inputlist)
    start = 0
    end = listsize - 1
    mid = 0
    while mid <= end: 
        if inputlist[mid] == 0: 
            inputlist[start],inputlist[mid] = inputlist[mid],inputlist[start] 
            start = start + 1
            mid = mid + 1
        elif inputlist[mid] == 1: 
            mid = mid + 1
        else: 
            inputlist[mid],inputlist[end] = inputlist[end],inputlist[mid]  
            end = end - 1
    return inputlist


# In[2]:

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


# In[ ]:



