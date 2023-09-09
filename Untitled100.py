#!/usr/bin/env python
# coding: utf-8

# 1. Why are functions advantageous to have in your programs?
# 2. When does the code in a function run: when it's specified or when it's called?
# 3. What statement creates a function?
# 4. What is the difference between a function and a function call?
# 5. How many global scopes are there in a Python program? How many local scopes?
# 6. What happens to variables in a local scope when the function call returns?
# 7. What is the concept of a return value? Is it possible to have a return value in an expression?
# 8. If a function does not have a return statement, what is the return value of a call to that function?
# 9. How do you make a function variable refer to the global variable?
# 10. What is the data type of None?
# 11. What does the sentence import areallyourpetsnamederic do?
# 12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
# 13. What can you do to save a programme from crashing if it encounters an error?
# 14. What is the purpose of the try clause? What is the purpose of the except clause?
# 
# 

# 
# 1. Functions are advantageous in programs for several reasons:
#    - Reusability: Functions allow you to encapsulate a block of code that can be reused multiple times.
#    - Modularity: Functions promote modular code design, making it easier to maintain and understand.
#    - Abstraction: Functions can hide complex operations and provide a simpler interface.
#    - Parameterization: Functions can accept parameters, making them versatile for various inputs.
# 
# 

# 
# 
# 2. The code in a function runs when it's called, not when it's specified. Functions are executed when they are invoked using their name followed by parentheses.
# 
# 

# 
# 3. The `def` statement is used to create a function in Python. For example:
#    
# 

# In[17]:



   def my_function(a,b):
       # Function code here
    return a+b
  


# In[18]:


my_function(2,3)


# 
# 
# 4. A function is a reusable block of code defined using the `def` statement. A function call is when you invoke or execute that function by using its name followed by parentheses with optional arguments. The call executes the code inside the function.
# 
# 

# 
# 5. In a Python program, there is one global scope and multiple local scopes. Each function defines its own local scope, and there's also a built-in scope.
# 
# 

# 6.When a function call returns, the variables in its local scope are destroyed, and their values are no longer accessible.

# 7.A return value is the value that a function sends back to the caller. It is typically specified using the return statement in a function. Yes, you can use the return value in an expression. For example:
# 
# result = my_function()
# 

# 8.If a function does not have a return statement, its return value is None.

# 9.To make a function variable refer to a global variable, you can use the global keyword inside the function. For example:
# 
# 

# In[16]:


global_var = 10

def my_function():
    global global_var
    global_var = 20

my_function()
print(global_var)  


# 10.The data type of None is NoneType.

# 11.The sentence import areallyourpetsnamederic would attempt to import a Python module named "areallyourpetsnamederic." If such a module exists, you can use its functions, classes, or variables in your code

# 12.If you had a bacon() function in a spam module, you would call it after importing spam like this:
# 
# import spam
# 
# result = spam.bacon()

# 13.To save a program from crashing when it encounters an error, you can use exception handling. Place the potentially problematic code within a try block and handle the error cases in an except block. This prevents the program from abruptly terminating.

# 14.The purpose of the try clause in exception handling is to enclose code that might raise an exception. The purpose of the except clause is to specify how to handle exceptions that are raised within the try block. It defines the actions to be taken when a specific exception occurs.

# In[ ]:




