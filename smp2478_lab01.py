"""
Name        :   Shivani Panchiwala
UTA ID      :   1001982478
Version     :   Python 3.11.1 64-bit
OS          :   Windows 11
"""


import os
def get_size(p=''):

    size = 0      # Store the Size 

    if p == '':      # if path is empty then it will access the current directory
        curr_dir = os.getcwd()
    else:
        curr_dir = p

    
    list_contents = os.listdir(curr_dir)     # list of all the contents in the given directory

    for item_name in list_contents:
        
        full_p = os.path.join(curr_dir, item_name)    # gives the full path of the item

        if os.path.isfile(full_p):       # if the path is a File then isfile func returns True
            print('File = ' + item_name + ' has size = ' + str(os.path.getsize(full_p)) + ' Bytes')
            size += os.path.getsize(full_p)

        elif os.path.isdir(full_p):      #  if the path is a Directory then isdir func returns True
            print('Directory found -> ' + item_name)
            size += get_size(full_p) # recursion to access sub-directories
            print('----------------')
        else:
            exception_msg = 'Item = ' + item_name + ' is not a file or directory'
            print(exception_msg)

    return size


def main():
    size = get_size()
    print('*********************************')
    print('Total Size = ' + str(size) + ' Bytes')
    print('*********************************')


if __name__ == '__main__':
    main()




"""
Code Explanation
----------------
The current directory is explored for its contents when If no path is mentioned.
If the item is a file then its size is stored and if it is directory the same function is called with the directory's path.
This recursion stops when all directories have been explored and file sizes stored.
The final size is returned.
"""

"""

1) Was one language easier or faster to write the code for this? If so, describe in detail why, as in what about the language made that the case.

I did the Lab in Python, Java and C++. 
For this task, using Python was the easiest and fastest approach for me because, Python has os library which provides all the required in-built functions made the task easy.
But Java was a quite competition.
C++ took the most time.

--------------------------------------------------------------------
2) Even though a language may not (e.g. FORTRAN) does not support recursion, describe how you could write a program to produce the same results without using recursion. 
Would that approach have any limitations and if so, what would they be?

1. We can start by accessing a given path and fetching its contents
2. These contents can be stored in an array of strings (file/directory paths)
3. If the item is a file, then we store its size.
4. If the item is a directory, then we can access its contents and add to our array we used earlier.
5. This happens for every directory until all directories are accessed.
6. The program must run in loop until the entire array containing paths has been traversed.
Limitations
1. The space complexity of this program will can be large as we are storing all the file/ directory paths.
2. It can be more hard to understand compared to the recursive approach.s
https://github.com/AmlanAlok/Programming-Language-Concepts/tree/main/lab-01
"""
