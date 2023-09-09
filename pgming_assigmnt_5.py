#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python Program to Find LCM?
# 

# In[25]:



def cal_lcm(n,m):
    
    if n==m:
        g=n
    elif n>m:
        g=n
    else:
        g=m

    while(True):
        if (n%g==0) and (m%g ==0):
            lcm=g
            break
        g+=1
    return lcm



n=int(input('Enter 1st value'))
m=int(input('Enter 2nd value'))
print('The Lcm is',cal_lcm(n,m))


# In[27]:


def calc_lcm(x,y):
    if x>y:
        l=x
    else:
        l=y
        
    while(True):
        if (x%l==0) and (y%l==0):
            lcm=l
            break
        l+=1
        
    return lcm


x=int(input('Enter 1st value'))
y=int(input('Enter 2nd vlue'))
print('lcm of 2 number is',calc_lcm(x,y))


# 
# 2.	Write a Python Program to Find HCF?

# In[24]:


def cal_hcf(x,y):
    if x>y :
        s=y
    else:
        s=x
        
        
    for i in range(1,s+1):
        if (x%i==0)and(y%i==0):
            hcf=i
    return hcf

x=int(input('enter a number'))
y=int(input('enter 2nd number'))

print('Hcf of given 2 number is',cal_hcf(x,y))
        


# 
# 3.	Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
# 

# In[37]:


def dec_binary(d):
    decimal=int(d)
    print('Decimal number',decimal,' to binary is',bin(decimal))
    
def dec_octal(d):
    decimal=int(d)
    print('Decimal number',decimal,' to Octal is',oct(decimal))
    
def dec_hexa(d):
    decimal=int(d)
    print('Decimal number',decimal,'to Hexadecimal is',hex(decimal))
    
    
d=int(input('Enter a number'))
dec_binary(d)
dec_octal(d)
dec_hexa(d)


# 
# 4.	Write a Python Program To Find ASCII value of a character?
# 
# 

# In[42]:


c=input('Enter a character')
print('The ASCII value of',c ,'is',ord(c))


# 
# 5.	Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
# 

# In[33]:


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if a>b:
        d=a*b
    else:
        d="division not possible"
        


print("Enter a choice")
print("1. Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

c=int(input("Enter the Chioce 1/2/3/4"))
a=int(input('Enter the 1st number'))
b=int(input('Enter 2nd number'))
if c==1:
    print('Addition result of ',a,'and',b,'is',add(a,b))
    
elif c==2:
    print('substraction result of ',a,'and',b,'is',sub(a,b))
    
elif c==3:
    print('Multiplication result of ',a,'and',b,'is',mul(a,b))
    
elif c==4:
    print('Division result of ',a,'and',b,'is',div(a,b))
    
else:
    
    print('The choice entered is wrong')


# 

# In[ ]:




