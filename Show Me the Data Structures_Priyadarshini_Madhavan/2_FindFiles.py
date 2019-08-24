
# coding: utf-8

# In[1]:

import os

def find_files(filepath, suffix):
    lis1_paths =[]
    if os.path.exists(filepath):
        suffix = suffix.lower()
        for dir, dirnames, files in os.walk(filepath):
            for name in files:
                if suffix and name.lower().endswith(suffix):
                    lis1_paths.append(os.path.join(dir, name))
                elif not suffix:
                    lis1_paths.append(os.path.join(dir, name))
        return lis1_paths
    else:
        return("Empty or Non-existent  File Path")
#path ='C:\\Users\\Priyadarshini\\new\\testdir' # location of the the sample file given by Udacity
path = './testdir' # location of the the sample file given by Udacity


# In[2]:

print(find_files(path,".c"))


# In[3]:

print(find_files(path,".h"))


# In[4]:

print(find_files(path,".z"))


# In[5]:

path = "./no-path"
print(find_files(path,".h"))


# In[6]:

path = ""
print(find_files(path,".h"))


# In[ ]:



