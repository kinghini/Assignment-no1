#!/usr/bin/env python
# coding: utf-8

# 1.Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.
# Examples
# equal(3, 4, 3) ➞ 2
# 
# equal(1, 1, 1) ➞ 3
# 
# equal(3, 4, 1) ➞ 0 
# Notes
# Your function must return 0, 2 or 3.
# 

# In[13]:


def fn1(a,b,c):
    if a!=b!=c:
        return 0
    elif a!=b==c:
        return(2)
    elif a==b!=c:
        return (2)
    elif a==c!=b:
        return (2)
    elif a==b==c:
        return (3)
    
        


# In[14]:


fn1(2,1,1)


# In[ ]:





# 2.Write a function that converts a dictionary into a list of keys-values tuples.
# Examples
# dict_to_list({
#   "D": 1,
#   "B": 2,
#   "C": 3
# }) ➞ [("B", 2), ("C", 3), ("D", 1)]
# 
# dict_to_list({
#   "likes": 2,
#   "dislikes": 3,
#   "followers": 10
# }) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]
# Notes
# Return the elements in the list in alphabetical order.
# 
# 

# In[16]:


def fn2(d):
    return(sorted(d.items()))


# In[17]:


fn2({'abc':123,'fgg':433,'efg':34})


# 3.Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.
# Examples
# mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
# 
# mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
# 
# mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
# Notes
# All of the letters in the input list will always be lowercase.
# 

# In[4]:


def fn3(l):
    return{m.lower():m.upper() for m in l}
    #for m in l:
        #d={m:m.upper()}
         #return(d)


# In[5]:


fn3(["a","b","K"])


# 4:Write a function, that replaces all vowels in a string with a specified vowel

# In[19]:


def fn4(s,vowel):
    vow="aeiouAEIOU"
    n=""
    for i in s:
        if i  in vow:
            n+=vowel
        else:
            n+=i
    return(n)


# In[21]:


fn4('saap','o')


# 5.Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.

# In[22]:


def fn5(s):
    n=""
    for j in s:
        if ord(j)%2 == 0:
            n+=j.upper()
        else:
            n+=j.lower()
    return n


# In[24]:


fn5("Hello")


# In[ ]:




