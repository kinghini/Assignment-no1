#!/usr/bin/env python
# coding: utf-8

# 1. To what does a relative path refer?
# 2. What does an absolute path start with your operating system?
# 3. What do the functions os.getcwd() and os.chdir() do?
# 4. What are the . and .. folders?
# 5. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?
# 6. What are the three “mode” arguments that can be passed to the open() function?
# 7. What happens if an existing file is opened in write mode?
# 8. How do you tell the difference between read() and readlines()?
# 9. What data structure does a shelf value resemble?

# 
# 
# 1. A **relative path** refers to a file or directory location in relation to the current working directory. It does not start from the root directory and depends on the current working directory.
# 

# 2. An **absolute path** starts with the root directory of the operating system. On Windows, it typically starts with a drive letter (e.g., `C:\`) followed by the full path to the file or directory. On Unix-like systems (including Linux and macOS), it starts from the root directory `/`.
# 

# 3. - `os.getcwd()`: This function returns the current working directory, which is the directory from which your Python script is currently executing.
#    - `os.chdir(path)`: This function changes the current working directory to the specified `path`, allowing you to navigate the file system.

# 4. - `.` (dot) represents the current directory.
#    - `..` (double dot) represents the parent directory of the current directory.
# 
# 

# 5. In `C:\bacon\eggs\spam.txt`, the **directory name** is `C:\bacon\eggs`, and the **base name** (file name) is `spam.txt`.
# 
# 

# 6. The three "mode" arguments that can be passed to the `open()` function are:
#    - `'r'`: Read mode (default). Opens the file for reading.
#    - `'w'`: Write mode. Opens the file for writing. If the file exists, it truncates (clears) the file. If the file doesn't exist, it creates a new empty file.
#    - `'a'`: Append mode. Opens the file for writing but does not truncate it. New data is appended to the end of the file.
# 
# 

# 7. If an existing file is opened in **write mode** (`'w'`), it will be truncated (all existing content will be deleted), and you will start writing from the beginning. Be cautious when using write mode on an existing file if you want to preserve the existing data.
# 
# 

# 8. - `read()`: Reads the entire contents of a file as a single string.
#    - `readlines()`: Reads the file line by line and returns a list of strings, with each element representing a line from the file.
# 

# 
# 9. A **shelf value** in Python resembles a **dictionary** data structure. A shelf is a persistent, dictionary-like storage format provided by the `shelve` module. It allows you to store and retrieve data using key-value pairs, similar to a dictionary. However, the data in a shelf is stored on disk and can be used to maintain data across multiple program runs.
