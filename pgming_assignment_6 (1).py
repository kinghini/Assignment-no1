#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# 1.	Write a Python Program to Display Fibonacci Sequence Using Recursion?
# 
# 
# Recursion is a common mathematical and programming concept. It means that a function calls itself.

# In[7]:


def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
#n=[0,1,2,3]
for i in range(10):
    print(f"fibonacci({i})= {fibonacci(i)}")


# 2.	Write a Python Program to Find Factorial of Number Using Recursion?
# 

# In[12]:


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

#n=6
n=int(input('Enter a number'))
print(f"factorial({n})= {factorial(n)}")


# 
# 3.	Write a Python Program to calculate your Body Mass Index?
# 

# In[27]:


def cal_bmi(weight,height):
    bmi=weight/(height)
    return(bmi)

weight=int(input('Enter your weight value'))
height= int(input('Enter your height value'))

bmi=cal_bmi(weight,height)

print(f" your weight{weight}kg and your height{height}m")
print(f" your Body Mass Index is {bmi}.")


# 
# 4.	Write a Python Program to calculate the natural logarithm of any number?
# 

# In[28]:


import math
a=int(input('Enter a number'))
base=int(input('Enter base value'))

if n<0:
    print('Given number is negative')
else:
    l=math.log(a,base)
    
print('The logarithmic value of ',a,'to the base',base,'is',l)


# 
# 5.	Write a Python Program for cube sum of first n natural numbers?

# In[3]:


def cub_sum(n):
    if n==1:
        return 1
    else:
        s=n**3+cub_sum(n-1)
    return s

#n=10
n= int(input('Enter the value of n'))
print(f" cube sum of {n} is {cub_sum(n)}")


# In[ ]:





# In[ ]:





# 
