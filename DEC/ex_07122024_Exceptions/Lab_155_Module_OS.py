import  os

print(os.getcwd())
# return the current working directory

#list the files in the current directory
files = os.listdir('/Users/varti/PycharmProjects/PYATB5xLearning/')
print(f"file in current directory:{files}")


#create a new directory

#os.mkdir('Test2')

#check to file exist

file_exist = os.path.exists("TestData.txt")
print(file_exist)

print(os.name)  #nt name for os  nt = windows