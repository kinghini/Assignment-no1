#!/usr/bin/env python
# coding: utf-8

# Question 1
# Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.

# In[16]:


def fn1(n):
    n=str(n)
    m=str(n[::-1])
        
    if m==n:
        return('Given number is symmertrical')
    else:
        return('Given number is Asymmertrical')


# In[24]:


print(fn1(3133))


# 2.
# Given a string of numbers separated by a comma and space, return the product of the numbers.

# In[55]:


def fn2(k):
    m=1
    n=[]
    for j in k.split(","):
         n.append(int(j))
    for i in  range(len(n)):
        m*=n[i]
    return(m)


# In[56]:


fn2("1,2,8,3")


# 3.Create a function that squares every digit of a number.

# In[68]:


def fn3(n):
    s=''
    for j in str(n):
        r=(int(j)**2)
        s+=str(r)
    return(int(s))


# In[69]:


fn3(1223)


# Question 4
# Create a function that sorts a list and removes all duplicate items from it.

# In[38]:


def fn4(l):
    s=sorted(l)
    e=[]
    for i in s:
        if i not in e:
            e.append(i)
    return e


# In[39]:


fn4([1,3,4,4])


# Question 5
# Create a function that returns the mean of all digits.

# In[63]:


def fn5(n):
    s=str(n)
    l=len(s)
    sd=0
    for i in s:
        sd+=int(i)
        m=(sd)/l
    return(m)


# In[64]:


fn5(42)


# In[ ]:





# In[ ]:




