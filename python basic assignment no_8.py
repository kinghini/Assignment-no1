#!/usr/bin/env python
# coding: utf-8

# 1. Is the Python Standard Library included with PyInputPlus?
# 2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?
# 3. How do you distinguish between inputInt() and inputFloat()?
# 4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?
# 5. What is transferred to the keyword arguments allowRegexes and blockRegexes?
# 6. If a blank input is entered three times, what does inputStr(limit=3) do?
# 7. If blank input is entered three times, what does inputStr(limit=3, default=&#39;hello&#39;) do?

# 
# 1. The feature responsible for generating Regex objects is the `re` module in Python.
# 

# 2. Raw strings (e.g., `r'\d'`) are often used in Regex objects because they prevent Python from interpreting backslashes as escape characters. This ensures that the regex pattern is treated as a raw string, making it easier to write and maintain.
# 
# 

# 3. The `search()` method returns a match object if a match is found, and `None` if no match is found.
# 
# 

# 4. To get the actual strings that match the pattern from a Match object, you can use the `.group()` method. For example, `match.group()` will return the entire matched string.
# 
# 

# 5. In the regex pattern `r'(\d\d\d)-(\d\d\d-\d\d\d\d)'`, group 0 covers the entire matched string, group 1 covers the first three digits, and group 2 covers the remaining digits in the phone number.
# 

# 6. To match real parentheses and periods in a regex, you can escape them using a backslash (`\(` for `(` and `\.` for `.`).
# 
# 

# 
# 7. The `findall()` method returns a list of all non-overlapping matches in the input string. It returns a list of strings when there are no capturing groups in the pattern and a list of tuples when there are capturing groups.
# 

# 
# 8. In standard expressions, the `|` character represents an OR operator, allowing you to match one of several alternatives in the pattern. For example, `r'cat|dog'` matches either 'cat' or 'dog'.
# 
# 

# 
# 9. In regular expressions, the `\d` shorthand character class signifies any digit (0-9).
# 
# 

# 10. In regular expressions, the `+` character matches one or more occurrences of the preceding element, while the `*` character matches zero or more occurrences.

# 11. `{4}` in a regular expression matches exactly four occurrences of the preceding element, whereas `{4,5}` matches between four and five occurrences.
# 
# 

# 12. In regular expressions, the shorthand character classes:
#     - `\d` matches any digit (0-9).
#     - `\w` matches any word character (alphanumeric plus underscore).
#     - `\s` matches any whitespace character (space, tab, newline, etc.).
# 
# 

# 13. In regular expressions, the shorthand character classes:
#     - `\D` matches any non-digit character.
#     - `\W` matches any non-word character.
#     - `\S` matches any non-whitespace character.
# 
# 

# 14. `.*?` is a non-greedy version of `.*`, which matches as few characters as possible while still allowing the overall pattern to match.
# 
# 

# 15. To match both numbers and lowercase letters with a character class, you can use `[0-9a-z]` or `[a-z0-9]`.
# 

# 16. To make a regular expression case insensitive, you can use the `re.IGNORECASE` or `re.I` flag when compiling the regex using `re.compile()`.
# 
# 

# 17. The `.` character normally matches any character except a newline. If `re.DOTALL` is passed as the second argument in `re.compile()`, `.` will match any character, including a newline.
# 
# 

# 18. `numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen')` will return `'X drummers, X pipers, five rings, X hen'`.
# 
# 

# 19. Passing `re.VERBOSE` as the 2nd argument to `re.compile()` allows you to add whitespace and comments to the regex pattern to make it more readable without affecting its functionality.
# 
# 

# 20. You can use the following regex to match numbers with commas for every three digits:
#     

# 
#     r'^\d{1,3}(,\d{3})*$'
# 

# 
# 
# 21. You can use the following regex to match the full name of someone whose last name is Watanabe:
#     

# In[24]:


r'[A-Z][a-z]*\sWatanabe'


# In[ ]:




22. You can use the following case-insensitive regex to match the described sentence:
   


# In[23]:




    r'^(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$'
   


# In[ ]:




