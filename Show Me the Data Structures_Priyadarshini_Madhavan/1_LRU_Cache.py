
# coding: utf-8

# In[1]:

import collections


# In[2]:

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return key
        except KeyError:
            return -1

    def setting_value(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value


# In[3]:

our_cache = LRUCache(5)
#our_cache.setting(key,value)
our_cache.setting_value(1, 1)
our_cache.setting_value(2, 2)
our_cache.setting_value(3, 3)
our_cache.setting_value(4, 4)
our_cache.setting_value(5, 5)


# In[4]:

our_cache.get(1)     # returns 1


# In[5]:

our_cache.get(2)     # returns 2


# In[6]:

our_cache.get(3)      # returns 3


# In[7]:

our_cache.get(7)     # returns -1


# In[8]:

our_cache.get(5)     ## returns 5


# In[9]:

our_cache.setting_value(6,6)


# In[10]:

our_cache.get(4)
# (6,6) was added which is beyond the LRU capacity, so the elememnt 4 got popped in the previous opertaion   
# 4 is the least recently & hence returned -1


# In[11]:

our_cache.get(None) ## None Key type edge case should return -1


# In[12]:

our_cache.get('') # empty string edge case returns -1


# In[ ]:



