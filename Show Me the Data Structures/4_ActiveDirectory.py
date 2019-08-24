
# coding: utf-8

# In[1]:

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


# In[2]:

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

child_user = "child_user"
child.add_user(child_user)


# In[3]:

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if  isinstance(group, Group):
        if user == group.get_name():
            return True
        if user in group.get_users():
            return True
        for val in group.get_groups():
            return is_user_in_group(user, val)
        return False
    else:
        return (str(group), "is not a valid Group")


# In[4]:

#sub_child_user is a user in sub_child group so it returns True
print(is_user_in_group("sub_child_user", sub_child))


# In[5]:

print(is_user_in_group ("sub_child_user",child))


# In[6]:

#child_user is a user in child group so it returns True
print(is_user_in_group("child_user", child))


# In[7]:

# Since 2nd parameter is not a  group , error message is printed
print(is_user_in_group(sub_child_user, child_user))


# In[ ]:




# In[ ]:



