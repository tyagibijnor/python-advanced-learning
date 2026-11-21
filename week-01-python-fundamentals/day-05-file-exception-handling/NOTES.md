What is File Handling?
Definition: File handling is the process of creating, reading, writing, updating and deleting files using a programming language.

Why do we need it?
- Store application data permanently.
- Read configuration files.
- Save application logs.
- Process CSV and JSON datasets.
- Store AI application inputs and outputs.

Basic syntax
file = open("example.txt", "r")content = file.read()file.close()



But professional Python code should generally use with.
with open("example.txt", "r") as file:    content = file.read()



Why? Python automatically closes the file, even if an exception occurs.
B. File opening modes
Mode	Meaning
r	Read existing file
w	Write; overwrite existing content
a	Append content
x	Create a new file; fail if it exists
r+	Read and write
rb	Read binary file
wb	Write binary file

Remember: w can erase existing content!
C. Important file methods
file.read()        # Read complete contentfile.readline()    # Read one linefile.readlines()   # Read all lines into a listfile.write("Hi")   # Write contentfile.seek(0)       # Move file cursorfile.tell()        # Get cursor position

What is an exception?
An exception is an error that occurs during program execution and interrupts the normal flow of the program.

Important exception keywords
Keyword	Purpose
try	Code that may fail
except	Handle an exception
else	Execute if no exception occurs
finally	Execute whether an exception occurs or not
raise	Manually raise an exception