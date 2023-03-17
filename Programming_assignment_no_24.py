#!/usr/bin/env python
# coding: utf-8

# Question1
# Create a function that takes an integer and returns a list from 1 to the given number, where:
# 1.	If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
# 2.	If the number cannot be divided evenly by 4, simply return the number.
# Examples
# amplify(4) ➞ [1, 2, 3, 40]
# 
# amplify(3) ➞ [1, 2, 3]
# 
# amplify(25) ➞ [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240, 25]
# 
# 

# In[99]:


def fn1(n):
    b=[]
    l=list(range(1,n+1))
    for j in l:
        if (j%4)==0:
            a=10*j
        else:
            a=j
        b.append(a)
    return(b)


# In[100]:


fn1(10)


# 2.Question2
# Create a function that takes a list of numbers and return the number that's unique.
# 

# In[123]:


def fn2(l):
    c={}
    for i in l:
        if i in c:
            c[i]+=1
        else:
            c[i]=1
    for j in c:
        if c[j]==1:
            return(j)
        
            
        


# In[128]:


fn2([2,3,4,3,2])


# Question3 Your task is to create a Circle constructor that creates a circle with a radius provided by an argument. The circles constructed must have two getters getArea() (PIr^2) and getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference). For help with this class, I have provided you with a Rectangle constructor which you can use as a base example. Examples circy = Circle(11) circy.getArea()

# In[75]:


import math
class circle:
    def __init__(self,r):
        self.r=r
        
    def getArea(self):
        A=math.pi*self.r**2
        return(A)
    
    def getPerimeter(self):
        p=2*math.pi*self.r
        return(p)
    


# In[77]:


c=circle(4)
print(c.getArea())
print(c.getPerimeter())


# In[ ]:





# Question4 Create a function that takes a list of strings and return a list, sorted from shortest to longest. Examples sort_by_length(["Google", "Apple", "Microsoft"]) ➞ ["Apple", "Google", "Microsoft"]
# 
# sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]) ➞ ["Raphael", "Leonardo", "Donatello", "Michelangelo"]
# 
# sort_by_length(["Turing", "Einstein", "Jung"]) ➞ ["Jung", "Turing", "Einstein"] Notes All test cases contain lists with strings of different lengths, so you won't have to deal with multiple strings of the same length.

# In[38]:


def fn4(l):
    b=len(l)
    for i in range(b-1):
        for  j in range(0,b-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return(l)
               


# In[39]:


fn4(['a','ab','abc'])


# Question5 Create a function that validates whether three given integers form a Pythagorean triplet. The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.

# In[69]:


def fn5(x,y,z):
    b=sorted([x,y,z])
    for i in range(len(b)-2):
        if (b[i])**2+(b[i+1])**2==(b[i+2])**2:
            return('Pythagorean triplet')
        else:
            return('Not a Pythagorean triplet')
                                  
                                  


# In[71]:


fn5(5,3,4)


# In[ ]:





# In[ ]:




