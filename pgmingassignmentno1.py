#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to print "Hello Python"?
# 

# In[3]:


print("Hello Python")


# 2.	Write a Python program to do arithmetical operations addition and division.?
# 

# In[26]:


a= float(input('enter the value of a'))
b= float(input('enter the value of b'))
c=a+b
#if b!=0:
d= a/b
#else:
    #print ('addition not possible')
print('result of additon of a&b is',c)
print('result of division of a&b is',d)


# 
# 3.	Write a Python program to find the area of a triangle?
# 

# In[27]:


l= float(input('enter the value of length'))
b=float(input('enter the value of breadth'))
A=(.5)*l*b
print('Area of triangle is',A)


# 
# 4.	Write a Python program to swap two variables?
# 
# 
# 

# In[28]:


x= input('enter the value of x')
y=input('enter the value o f y')
print('values of x and y before swaping ',x,y)
x,y=y,x
print('values of x and y after swaping',x,y)


# 5.	Write a Python program to generate a random number?

# In[34]:


import random
m= random.randint(1,10)
print('random number is ',m)


# In[ ]:




