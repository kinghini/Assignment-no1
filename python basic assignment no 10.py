#!/usr/bin/env python
# coding: utf-8

# 1. How do you distinguish between shutil.copy() and shutil.copytree()?
# 2. What function is used to rename files??
# 3. What is the difference between the delete functions in the send2trash and shutil modules?
# 4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is
# equivalent to File objects’ open() method?
# 5. Create a programme that searches a folder tree for files with a certain file extension (such as .pdf
# or .jpg). Copy these files from whatever location they are in to a new folder.

# 
# 1. **`shutil.copy()`** is used to copy a single file from one location to another. It takes two arguments: the source file path and the destination file path.
# 
#    **`shutil.copytree()`** is used to copy an entire directory and its contents from one location to another. It takes two arguments: the source directory path and the destination directory path. It recursively copies all files and subdirectories within the source directory.
# 
# 
# 

# 2. The **`shutil.move()`** function is used to rename files and directories in Python. It can also be used to move files and directories to a different location while renaming them if needed.
# 
# 

# 
# 3. The difference between the delete functions in the `send2trash` and `shutil` modules is how they handle deleted files:
# 
#    - **`shutil`**: The `shutil` module provides functions like `shutil.rmtree()` to delete files and directories, but they delete files permanently, and there is no way to recover them from the system's trash or recycle bin.
# 
#    - **`send2trash`**: The `send2trash` module, on the other hand, sends files and directories to the system's trash or recycle bin, depending on the operating system. This allows for potential recovery of deleted files from the trash or recycle bin.
# 
# 

# 
# 
# 4. The **`ZipFile`** object's **`open()`** method is equivalent to File objects' **`open()`** method. It is used to open and access the contents of a ZIP archive. You can use it to read, write, or manipulate the files within the ZIP archive.
# 

#  5.Here's a Python program that searches a folder tree for files with a certain file extension (e.g., `.pdf` or `.jpg`) and copies them to a new folder:
# 

# In[9]:


import os
import shutil
 
def copy_files_with_extension(source_folder, extension, destination_folder):
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.endswith(extension):
                source_path = os.path.join(foldername, filename)
                destination_path = os.path.join(destination_folder, filename)
                shutil.copy(source_path, destination_path)


# In[ ]:





# In[ ]:




