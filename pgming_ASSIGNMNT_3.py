#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
# 

# In[2]:


N=int(input('enter a nuber'))

if N==0:
    print('Given number is zero')
else:
    if N>0:
        print(N,'Given number  is possitive')
    else:
        print(N,'Given number is negative')

    


# 
# 2. Write a Python Program to Check if a Number is Odd or Even?
# 

# In[12]:


K= int(input('enter a number'))
if K%2 ==0:
    print(K,'number is even')
else:
    print(K,'Number is odd')


# 
# 3. Write a Python Program to Check Leap Year?
# 

# In[18]:


y=int(input('enter a year'))
if y%4==0:
    print(y,'given year is leap year')
else:
    print(y,'given year is not leap year')


# 4. Write a Python Program to Check Prime Number?
# 

# In[15]:


M=int(input('Enter a Number'))
if M>1:
    for i in(range(2,M)):
        if M%i==0:
                print(M,'is not a prime number')
                break
        else:
            print(M,'is a prime number')
else:
    print("Given number is not a prime its negative number")


# In[24]:


m=int(input('enter  a number'))
if m<=1:
    print('Given number',m,'is not prime number')
else:
    for i in range(2,m):
        if (m%i)==0:
            print('Given number is not a prime number')
            break
    else:
              print('Given number',m,' is prime number')


# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[34]:



    print('All prime numbers in an interval 1-10000')
    for i in range(2,10000):
        for j in range(2,(i-1)):
            if (i%j)==0:
                break
        else:
        
                  print(i)
                  


# In[ ]:




