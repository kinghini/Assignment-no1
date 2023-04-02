#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to check if the given number is a Disarium Number?
# 
# To find whether given number is Disarium or not, calculate the sum of digits powered with their respective positions. If the sum is equal to the original number then, the given number is Disarium number.

# In[2]:


n= int(input('Enter a number'))
l=len(str(n))
s=0
t=n
while t>0:
    k=t%10
    s+=k**l
    l-=1
    t//=10
if s==n:
    print('Given number',n ,'is Disarium Number')
else:
    print('Given number',n ,'is not Disarium Number')


# 2.	Write a Python program to print all disarium numbers between 1 to 100?
# 

# In[7]:


print('Disarium Numbers between 1 to 100')
for i in range(1,101):
   n=i
   l=len(str(n))
   s=0
   t=i  
   while t>0:
       k=t%10
       s+=k**l
       l-=1
       t//=10
   if s==n:
           print(s)


# 3.	Write a Python program to check if the given number is Happy Number?
# 
# A happy number is the one that ends up as 1, when it is replaced by the sum of square of every digit in the number.

# In[35]:


def happy_num(n):
    sum_set=set()
    
    while n!=1:
        n=sum(int(i)**2 for i in str(n))
        if n in sum_set:
            return False
        sum_set.add(n)
    return True


# In[36]:


happy_num(19)


# 4.	Write a Python program to print all happy numbers between 1 and 100?
# 

# In[42]:


def happy_num(n):
    sum_set=set()
    
    while n!=1:
        n=sum(int(i)**2 for i in str(n))
        if n in sum_set:
            return False
        sum_set.add(n)
    return True

for i in range(1,101):
    if happy_num(i):
        print(i)
    
        


# In[34]:


happy_num(19)


# 5.	Write a Python program to determine whether the given number is a Harshad Number?
# 

# In[60]:


n= int(input('enter a number'))
#for i in range(len(n)):
s=sum(int(i) for i in str(n))
if n%s==0:
    print('Given number',n,'is Harshad Number')
else:
    print('Given number',n,'is not Harshad Number')


# 6.	Write a Python program to print all pronic numbers between 1 and 100?
# A pronic number is a number which is the product of two consecutive integers, that is, a number of the form n(n + 1). The first few pronic numbers are: 0, 2, 6, 12, 20, 30, 42, 56, 72,

# In[87]:


m=[]
print('Pronic numbers between 1 and 100')
for i in range(1,101):
    j=i*(i+1)
    m.append(j)
    for k in m:
        if i==k:
            print(k)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




