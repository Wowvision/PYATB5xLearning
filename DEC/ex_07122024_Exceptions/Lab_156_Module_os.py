import os
try:
    file_path = os.getcwd()
    print(file_path)
    file_full_path = file_path + '/example.txt'
    print(file_full_path)

# read the file
    file = open(file_full_path) #FileNotFoundError: [Errno 2] No such file or directory
                              #means example.txt does't exist
except Exception as fnfe:
    print("File not found , fix the path or create the file")
finally:
    #file.close()
    print("This code will be executed")

# read the file
#handle to this using try exept