#!/usr/bin/env python
# coding: utf-8

# ##pgming assignment no 4
# 1.	Write a Python Program to Find the Factorial of a Number?
# 2.	Write a Python Program to Display the multiplication Table?
# 3.	Write a Python Program to Print the Fibonacci sequence?
# 4.	Write a Python Program to Check Armstrong Number?
# 5.	Write a Python Program to Find Armstrong Number in an Interval?
# 6.	Write a Python Program to Find the Sum of Natural Numbers?
# 

# 1.	Write a Python Program to Find the Factorial of a Number?

# In[12]:


N=int(input('enter a number'))
if N<0:
    print('Negative number has no factorial')
else:
    f=1
    for i in range(1,N+1):

            f=f*i
    print('Factorial is',f)


# 2. Write a Python Program to Display the multiplication Table?

# In[20]:


n=int(input('enter the number'))
print('Multiplication table of',n,'is')
for i in range(1,11):
        k=i*n

        print(k)


# 3.Write a Python Program to Print the Fibonacci sequence?

# In[20]:


n=int(input('Enter no of elements in the fibonacci sequence'))
a=0
b=1
print('Fibonacci sequence of',n,'no of elements is')
for i in range(0,n):
    k=a+b  
    print(a)
    a=b
    b=k


# 4.Write a Python Program to Check Armstrong Number?

# In[38]:


n=int(input('Enter a number'))
k=len(str(n))
t=n
s=0
while t>0:
    a=t%10
    s+=a**k
    t//=10
if s==n:
    print('Given number is Armstrong Number')
else:
    print('Given number is  not Armstrong Number')


# Write a Python Program to Check Armstrong Number in  an intervel?
# 

# In[19]:


n=int(input('Enter 1st value of  intervel'))
m=int(input('Enter last value of  intervel'))
print('Armstrong number between',n,'and',m,)
for i in range(n,m+1):
    k=len(str(i))
    t=i
    s=0
    while t>0:
        a=t%10
        s+=a**k
        t//=10
        if s==i:
            print(s)

        


# 6.Write a Python Program to Find the Sum of Natural Numbers?

# In[8]:


N=int(input('enter no of natural numbers'))
m=int(input('enter method for summation 1 or 2'))
k=0
if m==1:

    s=(1/2)*N*(N+1)
    print(s)

elif m==2:
    for j in range(0,N+1): 
        k=k+j
    print('Sum of',N,'number is',k)
else:
    print('enter a valid method')
    


# In[13]:


for i in range(1,11):
    print(i)


# In[ ]:




