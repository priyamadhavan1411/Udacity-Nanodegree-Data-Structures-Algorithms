
# coding: utf-8

# In[1]:

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self,handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = '/'
        self.handler = handler
        self.next = dict()
        
    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current = self.next
        path = path.split('/')
        for parts in path:
            current.insert(RouteTrieNode(parts))
            current = current.next[parts]
        current.handler = handler

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if paths == '/':
            return self.handler
        else:
            return None
        paths = paths.split('/')

        for parts in paths:
            current = self
            for parts in paths:
                current = current.next
                current = current[parts]
            handler = current.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, value=''):
        # Initialize the node with children as before, plus a handler
        self.value = value
        self.handler = None
        self.next = {}

    def insert(self, next_path, handler=None):
        # Insert the node as before
        self.next[next_path] = self.next.get(next_path, RouteTrieNode(next_path))
        self.next[next_path].handler = handler


# In[2]:

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = '/'
        self.handler = root_handler
        self.next = {}
        self.not_found = not_found_handler

    def add_handler(self, path, path_handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if path == self.root:
            self.handler = path_handler
        else:
            path = self.split_path(path)
            current = self.next
            i = 1
            for parts in path:
                if not parts:
                    continue
                if i:
                    i = 0
                    current[parts] = current.get(parts, RouteTrieNode(parts))
                    current = current[parts]
                else:
                    current.insert(parts, path_handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == '/':
            return self.handler
        path = self.split_path(path)
        current = self
        for parts in path:
            if parts:
                if parts in current.next:
                    current = current.next
                    current = current[parts]
                else:
                    return self.not_found

        handler = current.handler
        if handler:
            return handler
        else:
            return 'not found handler'

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split('/')


# In[3]:

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler' 
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one -- 
print(router.lookup("/home/about")) # should print 'about handler' --- 
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


# In[ ]:




# In[ ]:



