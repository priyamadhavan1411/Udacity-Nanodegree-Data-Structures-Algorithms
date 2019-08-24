
# coding: utf-8

# In[1]:

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next
            
    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current
    
    def pop(self):
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next

def remove_Duplicate(llist):
    dict1 = dict()
    llist2 = LinkedList()
    
    llist_curr = llist.head
    while llist_curr:
        if llist_curr.value not in dict1:
            llist_curr.value = str(llist_curr.value)
            dict1 [llist_curr.value] = 1
        elif llist_curr.value in dict1:
            llist_curr.value = str(llist_curr.value)
            dict1 [llist_curr.value] += 1
        else:
            continue
        llist_curr = llist_curr.next
        
    for key in dict1:
        llist2.append(key)
    return llist2
    

def union(list1, list2):
    merged = LinkedList()
    
    list1_elt = list1.head
    list2_elt = list2.head
    
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list1_elt)
            merged.append(list2_elt)
            list1_elt = list1_elt.next
            list2_elt = list2_elt.next
    
    merged2 = remove_Duplicate(merged)
    return merged2

def intersection(list1, list2):
    
    intersection = LinkedList()
    if (list1.head is None or list2.head is None):
        return intersection
    
    current1 = list1.head
    while current1:
        current2 = list2.head
        value = current1.value
        while current2:
            if current2.value == value:
                node = Node(value)
                intersection.append(node)
                break
            current2 = current2.next
        current1 = current1.next
    intersection2 = remove_Duplicate(intersection)
    return intersection2


# In[2]:

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print (union(linked_list_1,linked_list_2)) # Expected Output 3 -> 6 -> 2 -> 32 -> 4 -> 35 -> 9 -> 65 -> 1 -> 11 -> 21 ->
print (intersection(linked_list_1,linked_list_2)) # Expected Output 4 -> 6 -> 21 -> 


# In[3]:

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [2,3,6,7,8,7]
element_2 = [1,3,2,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4)) # Expected Output 2 -> 1 -> 3 -> 6 -> 7 -> 8 -> 
print (intersection(linked_list_3,linked_list_4)) # Expected Output 2 -> 3 -> 


# In[4]:

# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [0,2,4,23]
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4)) # Expected Output 0 -> 2 -> 4 -> 23 -> 
print (intersection(linked_list_3,linked_list_4)) # Expected Output Returns nothing


# In[6]:

# Test case 4

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = ""
element_2 = [2]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4)) # Expected Output  2 -> 
print (intersection(linked_list_3,linked_list_4)) # Expected Output Returns nothing


# In[ ]:



