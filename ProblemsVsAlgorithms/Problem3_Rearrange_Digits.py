
# coding: utf-8

# In[1]:

def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged


def rearrange_digits(items):
    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = rearrange_digits(left)
    right = rearrange_digits(right)
    
    l = merge(left, right)
    
    sum1 = [x for x in l if l.index(x) in range(0,len(l),2)]
    sum2 = [x for x in l if l.index(x) in range(1,len(l),2)]
    sum3 = int("".join(map(str, sum1)))
    sum4 = int("".join(map(str, sum2)))
    return [sum3,sum4]


# In[3]:

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]


# In[5]:

test_function([[1, 3, 4, 5], [53, 41]])
test_case = [[4, 2, 5, 9, 8], [952, 84]]


# In[6]:

test_function([[1, 3, 5], [51, 3]])
test_case = [[4, 2, 8], [84, 2]]


# In[ ]:



