
# coding: utf-8

# In[1]:

import sys, string
import sys
from collections import Counter
from operator import itemgetter

codes   = {}

#Take a string and determine the relevant frequencies of the characters.
#Build and sort a list of tuples from lowest to highest frequencies.
def create_freq(data):
    dict_freq = Counter(data)
    dict_freq = dict(Counter(data))
    list_tuples = [(v, k) for k, v in dict_freq.items()]
    list_tuples.sort(key=itemgetter(0))
    return list_tuples
    #print(list_tuples)

#Build the Tree by assigning of frequency values
def huffmantree(list_tuples) :
    if len(list_tuples)<=1:
        list
    
    while len(list_tuples) > 1 :
        firsttwo = tuple(list_tuples[0:2]) 
        remaining  = list_tuples[2:]  
        freqsum = firsttwo[0][0] + firsttwo[1][0] 
        list_tuples   = remaining + [(freqsum,firsttwo)] 
        list_tuples.sort(key=lambda t: t[0]) 
    return list_tuples[0]            # Return the single tree inside the list 

#Removing frequency counts & reducing tree
def trimTree(tree) :
    p = tree[1]                                    
    if type(p) == type("") : 
        return p              
    else : 
        return (trimTree(p[0]), trimTree(p[1])) 

#The heart of the huffman code - Assigning a binary code to each letter. 
def assignCode(node,pattern=" ") :
    if len(node)<=1:
        pattern="0"
    else:
        pattern=""
        
    global codes
    if type(node) == type(" ") :
        codes[node] = pattern                
    else:                               
        assignCode(node[0], pattern+"0")    
        assignCode(node[1], pattern+"1")     

def encode (str) :
    global codes
    output = ""
    for ch in str : output += codes[ch]
    return output

def decode (tree, str) :
    output = ""
    p = tree
    for bcode in str :
        if bcode == '0': 
            p = p[0]     
        else:
            p = p[1]    
        if type(p) == type(""):     
            output += p              
            p = tree                 
    return output



# In[2]:

def test_function(a_great_sentence):
    print ("The content of the data is: {}\n".format(a_great_sentence))
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
  
    if len(a_great_sentence) >= 1:
        tuples = create_freq(a_great_sentence)
        tree = huffmantree(tuples)
        tree = trimTree(tree)
        assignCode(tree)
        encoded_data= encode(a_great_sentence)
        
        print ("The content of the encoded data is: {}\n".format(encoded_data))
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        

        decoded_data = decode (tree, encoded_data)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))
    else:
        print("Invalid String")


# In[3]:

if __name__ == "__main__":
    
    print("TEST1 ###################################################")
    test_function("a great bird")
    print("TEST2 ###################################################")
    test_function ("AAAAA")
    print("TEST3 ###################################################")
    test_function ("")
   


# In[ ]:




# In[ ]:




# In[ ]:



