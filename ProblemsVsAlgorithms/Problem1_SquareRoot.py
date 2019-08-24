
# coding: utf-8

# In[1]:

#Problem 1: Square Root of an Integer


# In[3]:

def sqrt(number):
    low = 0
    high = number
    
    while low <=high:
        mid = (low+high)//2
        midsquared = mid*mid
        
        if midsquared <=number:
            low = mid +1 
        else:
            high = mid-1
            
    return low-1

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")


# In[ ]:



