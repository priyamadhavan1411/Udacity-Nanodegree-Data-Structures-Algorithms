
# coding: utf-8

# In[1]:

def get_min_max(input_list):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    maxnum = input_list[0]
    minnum = input_list[0]
    for num in input_list[1:]:
        if num > maxnum:
            maxnum = num
        elif num < minnum:
            minnum = num
        else:
            continue
    return (minnum,maxnum)              


# In[2]:

#Test case 1
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


# In[3]:

#Test case 2
l = [4,7,1,9,0,4,2,25,87,3,-1]

print ("Pass" if ((-1, 87) == get_min_max(l)) else "Fail")


# In[4]:

#Test Case 3
l =[i for i in range(0,21,2)]
random.shuffle(l)
print ("Pass" if ((0, 20) == get_min_max(l)) else "Fail")

