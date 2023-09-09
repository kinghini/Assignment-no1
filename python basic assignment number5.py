#!/usr/bin/env python
# coding: utf-8

# 1. What does an empty dictionary&#39;s code look like?
# 2. What is the value of a dictionary value with the key &#39;foo&#39; and the value 42?
# 3. What is the most significant distinction between a dictionary and a list?
# 4. What happens if you try to access spam[&#39;foo&#39;] if spam is {&#39;bar&#39;: 100}?
# 5. If a dictionary is stored in spam, what is the difference between the expressions &#39;cat&#39; in spam and
# &#39;cat&#39; in spam.keys()?
# 6. If a dictionary is stored in spam, what is the difference between the expressions &#39;cat&#39; in spam and
# &#39;cat&#39; in spam.values()?
# 7. What is a shortcut for the following code?
# if &#39;color&#39; not in spam:
# spam[&#39;color&#39;] = &#39;black&#39;
# 
# 8. How do you &quot;pretty print&quot; dictionary

# 1.Empty dictionary look like

# In[1]:


empty_dict = {}


# 2.The value of a dictionary with the key 'foo' and the value 42 would look like this:
#    

# In[3]:


my_dict = {'foo': 42}


# 3. The most significant distinction between a dictionary and a list is how they store and access data:
#    - **Dictionary:** Uses key-value pairs for data storage. Data is accessed by specifying a unique key, not an index. Dictionaries are unordered in Python versions before 3.7 and ordered from Python 3.7 onwards.
#    - **List:** Stores data in an ordered sequence and is accessed by index. Lists can contain elements of different data types.

# 4. If you try to access `spam['foo']` and `spam` is `{ 'bar': 100 }`, you will get a `KeyError` because there is no key 'foo' in the `spam` dictionary.
# 

# In[7]:


spam={'bar':100}
spam['foo']


# 5. If a dictionary is stored in `spam`, the expression `'cat' in spam` checks if the key 'cat' exists in the dictionary. The expression `'cat' in spam.keys()` essentially does the same thing, as it checks for the existence of the key 'cat' in the keys of the dictionary. There's no practical difference between the two expressions.
# 

# 6.If a dictionary is stored in `spam`, the expression `'cat' in spam` checks if the key 'cat' exists in the dictionary. On the other hand, the expression `'cat' in spam.values()` checks if 'cat' exists as a value in the dictionary. This means it will search for 'cat' among the values associated with the keys in the dictionary.
# 

# 7. A shortcut for adding a key-value pair to a dictionary if the key doesn't exist is to use the `setdefault()` method:
#    
#    spam.setdefault('color', 'black')
#  
#    This code will set the value for the 'color' key to 'black' only if 'color' does not already exist in the `spam` dictionary.

# In[9]:


spam.setdefault('color', 'black')
spam


# 8. To "pretty print" a dictionary (format it in a more readable way), you can use the `pprint` module from the `pprint` library:
#    ```python
#    import pprint
# 
#    my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
#    pprint.pprint(my_dict)
#    ```
#    This will format the dictionary with line breaks and indentation to make it more human-readable, especially for large dictionaries.

# In[6]:



   import pprint

   my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
   pprint.pprint(my_dict)
   


# In[ ]:




