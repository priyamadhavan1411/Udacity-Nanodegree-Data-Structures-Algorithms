
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[1]:

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.root = None
        self.data = None
        self.children = dict()
        self.is_word = False
    
    def insert(self, char, data=None):
        ## Add a child node in this Trie
        if not isinstance(char, TrieNode):
            self.children[char] = TrieNode(char, data)
        else:
            self.children[key.label] = key

    def all(self, prefix):
        if self.is_word:
            yield prefix

        for part, child in self.children.items():
            yield from child.all(prefix + part)
   
             
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node
    
    def suffixes(self, suffix = ''):
            ## Recursive function that collects the suffix for 
            ## all complete words below this point
        cur = self.root
        for c in suffix:
            cur = cur.children.get(c)
            if cur is None:
                return  # No words with given prefix

        yield from cur.all(suffix)


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[2]:

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.root = None
        self.data = None
        self.children = dict()
        self.is_word = False
    
    def insert(self, char, data=None):
        ## Add a child node in this Trie
        if not isinstance(char, TrieNode):
            self.children[char] = TrieNode(char, data)
        else:
            self.children[key.label] = key
            
    def all(self, prefix):
        if self.is_word:
            yield prefix

        for part, child in self.children.items():
            yield from child.all(prefix + part)
            
    def suffixes(self, suffix):
            ## Recursive function that collects the suffix for 
            ## all complete words below this point
        cur = self.root
        for c in suffix:
            cur = cur.children.get(c)
            if cur is None:
                return  # No words with given prefix

        yield from cur.all(suffix)
        


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[3]:

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory"]
for word in wordList:
    MyTrie.insert(word)


# In[4]:

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
           # print('\n'.join(prefixNode.suffixes()))
            needed = list(MyTrie.suffixes(prefix))
            final_list = []
            for a in needed:
                a = a.replace(prefix,'')
                final_list.append(a)
            while("" in final_list) : 
                final_list.remove("") 
            print (final_list)    
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[ ]:




# In[ ]:



