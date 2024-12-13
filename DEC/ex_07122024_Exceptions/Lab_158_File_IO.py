#how to create a file and write a content n W mode
import os
from tkinter.font import names

file_new = "Shubham.txt"

content ="This is a shubham file ABC"

with open(file_new,"w") as file:
    file.write(content)

#how to read a file in r mode

with open(file_new,"r") as file:
    content2= file.read()
    print(content2 )

# for the move the directory -> os.chdir("Desktop")

#remove a directory and file
#os.remove("path", file)
# os.removedirs(name of the directory)