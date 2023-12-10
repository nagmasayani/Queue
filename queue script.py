#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue

# Step 1: Create a Queue object
my_queue = queue.Queue()

# Step 2: Add an element to the Queue
my_queue.put("Compass")

# Step 3: Pop an element from the Queue
popped_element = my_queue.get()

# Step 4: Show the output
print("Popped element:", popped_element)

