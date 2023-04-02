#!/usr/bin/env python
# coding: utf-8

# 1.What are the two values of the Boolean data type? How do you write them?
#  The two values of Boolean data type are ‘0’ and ‘1’.
# We represent it as  True = 1,False=0
# 

# 2. What are the three different types of Boolean operators?
# The  logical operators  ‘AND’,’ OR’,  ‘ NOT’ are  also refered as Boolean operators

# 
3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
AND
Inputs	Output
0	0	0
0	1	0
1	0	0
1	1	1

OR
Inputs	Output
0	0	0
0	1	1
1	0	1
1	1	1



NOT
Input	Output
0	1
1	0
# 4. What are the values of the following expressions?
# 1)(5 > 4) and (3 == 5)
#              False
# 2)not (5 > 4)
#                 False
# 3)(5 > 4) or (3 == 5)
#                   True
# 4)not ((5 > 4) or (3 == 5))
#                     False
# 5)(True and True) and (True == False)
# 		False
# 6)(not False) or (not True)
# 		True

# 5. What are the six comparison operators?
# 	1)Greater than >
# 	2)Less than <
# 	3) Greater than or equal to >=
# 	4)Lessthan or equal to <=
# 	5)Equal to ==
# 	6) Not equal to !=

# 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
# 
# 

# The assignment operator is used to assign values in the  left hand side and right hand side
# =	==
# Assignment operator	Relational or comparison operator
# Assigning  values to a variable	Used for comparing two values it returns 1 if both values are equal else it returns zero
# Constant term is given on the right side	No place value 

# In[25]:



    A=10
    B=12
    C= A+B
    print('Result of addition  is',C)


# In[38]:



A=input('enter the value of A')
if A == 10:
    print('the value is  equal')
else :
    print('The given value is different')
    


# 7. Identify the three blocks in this code:
# 

# In[42]:


spam = 10
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')


# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
# 

# In[2]:


#spam= input('enter spam value')
spam=1
if spam == 1:
    print('Hello')
if spam == 2:
    print('Howdy')
else:
    print('Greetings!')
    


# 9.If your programme is stuck in an endless loop, what keys you’ll press?

# ctrl+C

# 10. How can you tell the difference between break and continue?

#    Break- It is used for termination of all the iterations in the loop
#             line which is just after the loop will gain control of program
#             It performs termination of the loop
# Continue- It is used for termination of only  current iteration in the loop
#            Control will pass to the next iteration of the current loop by skipping the current iteration
#            Early execution of the next loop

# In[113]:


for j in range(10):
    
    if j<5:
        
        print('break of loop occurs with value',j)
    break
print('end value of loop is',j)


# In[114]:


for j in range(10):
   
    if j<5:
        
        print('test condhition checked with value',j)
    continue 

print('end value of loop is',j)


# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

# In[ ]:


range(10)
This function gives 10  values,that satrts from 0 and ends in 9
range(0,10)
This function gives 10  values,that satrts from 0 and ends in 9,here starting value 0 is mentioned
range(0, 10, 1)
This function gives 10  values,that satrts from 0 and ends in 9,here stepvalue 1 is mentioned


# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[69]:


for i in range(1,11):
    print(i)


# In[3]:


n=0
while n<10:
    n=n+1
    print (n)


# 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# 

# spam bacon()
