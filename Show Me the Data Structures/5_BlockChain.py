
# coding: utf-8

# In[1]:

from datetime import datetime
import hashlib 

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
  
    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


# In[2]:

def time():
    time = datetime.now()
    return time.strftime("%d/%m/%Y %H:%M:%S")


# In[3]:

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
        else:
            current = self.last
            self.last = Block(timestamp, data, current)
            self.last.previous_hash = current


# In[4]:

blockchain = LinkedList()
blockchain.append(time(), "Adding initial data")
blockchain.append(time(), "Next Block1")
blockchain.append(time(), "Next Block2")
blockchain.append(time(), "Next Block3")
print(blockchain.last.previous_hash.data)
print(blockchain.last.data)
print(blockchain.last.timestamp)
print(blockchain.last.hash)


# In[ ]:



