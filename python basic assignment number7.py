#!/usr/bin/env python
# coding: utf-8

# 1. What is the name of the feature responsible for generating Regex objects?
# 2. Why do raw strings often appear in Regex objects?
# 3. What is the return value of the search() method?
# 4. From a Match item, how do you get the actual strings that match the pattern?
# 5. In the regex which created from the r&#39;(\d\d\d)-(\d\d\d-\d\d\d\d)&#39;, what does group zero cover?
# Group 2? Group 1?
# 6. In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell
# a regex that you want it to fit real parentheses and periods?
# 7. The findall() method returns a string list or a list of string tuples. What causes it to return one of
# the two options?
# 8. In standard expressions, what does the | character mean?
# 9. In regular expressions, what does the character stand for?
# 10.In regular expressions, what is the difference between the + and * characters?
# 11. What is the difference between {4} and {4,5} in regular expression?
# 12. What do you mean by the \d, \w, and \s shorthand character classes signify in regular
# expressions?
# 13. What do means by \D, \W, and \S shorthand character classes signify in regular expressions?
# 14. What is the difference between .*? and .*?
# 15. What is the syntax for matching both numbers and lowercase letters with a character class?
# 16. What is the procedure for making a normal expression in regax case insensitive?
# 17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd
# argument in re.compile()?
# 18. If numReg = re.compile(r&#39;\d+&#39;), what will numRegex.sub(&#39;X&#39;, &#39;11 drummers, 10 pipers, five rings, 4
# hen&#39;) return?
# 19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?
# 20. How would you write a regex that match a number with comma for every three digits? It must
# match the given following:
# &#39;42&#39;
# &#39;1,234&#39;
# &#39;6,368,745&#39;
# 
# but not the following:
# &#39;12,34,567&#39; (which has only two digits between the commas)
# &#39;1234&#39; (which lacks commas)
# 21. How would you write a regex that matches the full name of someone whose last name is
# Watanabe? You can assume that the first name that comes before it will always be one word that
# begins with a capital letter. The regex must match the following:
# &#39;Haruto Watanabe&#39;
# &#39;Alice Watanabe&#39;
# &#39;RoboCop Watanabe&#39;
# but not the following:
# &#39;haruto Watanabe&#39; (where the first name is not capitalized)
# &#39;Mr. Watanabe&#39; (where the preceding word has a nonletter character)
# &#39;Watanabe&#39; (which has no first name)
# &#39;Haruto watanabe&#39; (where Watanabe is not capitalized)
# 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob,
# or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs;
# and the sentence ends with a period? This regex should be case-insensitive. It must match the
# following:
# &#39;Alice eats apples.&#39;
# &#39;Bob pets cats.&#39;
# &#39;Carol throws baseballs.&#39;
# &#39;Alice throws Apples.&#39;
# &#39;BOB EATS CATS.&#39;
# but not the following:
# &#39;RoboCop eats apples.&#39;
# &#39;ALICE THROWS FOOTBALLS.&#39;
# &#39;Carol eats 7 cats.&#39;

# 
# 1. The feature responsible for generating Regex objects is the `re` module in Python.

# 2. Raw strings (e.g., `r'\d'`) are often used in Regex objects because they prevent Python from interpreting backslashes as escape characters. This ensures that the regex pattern is treated as a raw string, making it easier to write and maintain.

# 3. The `search()` method returns a match object if a match is found, and `None` if no match is found.
# 

# 4. To get the actual strings that match the pattern from a Match object, you can use the `.group()` method. For example, `match.group()` will return the entire matched string.
# 

# 5. In the regex pattern `r'(\d\d\d)-(\d\d\d-\d\d\d\d)'`, group 0 covers the entire matched string, group 1 covers the first three digits, and group 2 covers the remaining digits in the phone number.
# 
# 

# 6. To match real parentheses and periods in a regex, you can escape them using a backslash (`\(` for `(` and `\.` for `.`).
# 
# 

# 7. The `findall()` method returns a list of all non-overlapping matches in the input string. It returns a list of strings when there are no capturing groups in the pattern and a list of tuples when there are capturing groups.
# 
# 

# 8. In standard expressions, the `|` character represents an OR operator, allowing you to match one of several alternatives in the pattern. For example, `r'cat|dog'` matches either 'cat' or 'dog'.
# 
# 

# 9. In regular expressions, the `\d` shorthand character class signifies any digit (0-9).
# 
# 

# 10. In regular expressions, the `+` character matches one or more occurrences of the preceding element, while the `*` character matches zero or more occurrences.
# 

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

# 20. we can use the following regex to match numbers with commas for every three digits:
#     

# In[19]:


r'^\d{1,3}(,\d{3})*$'


# 21. we can use the following regex to match the full name of someone whose last name is Watanabe:
#     ```python
#     r'[A-Z][a-z]*\sWatanabe'
#     ```
# 
# 

# In[22]:


r'[A-Z][a-z]*\sWatanabe'


# In[20]:


22. we can use the following case-insensitive regex to match the described sentence:
    


# In[21]:



    r'^(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$'
   


# In[ ]:




