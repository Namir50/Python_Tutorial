#File is a container in computer system for storing data
#Data is permanently stored 
#Tpes of file: Text file and Binary file

#open: returns the file handle
#In order to perform any kind of operation we must first open the file 

f = open("C:\\Users\\namir\\OneDrive\\Documents\Python\\Python tutorial\\ex.txt")
print(type(f))
print(f.read())  #read the file
print(f.close()) #closes the file
print(f.closed) #returns a boolean if the file is closed 


#with open
#most common way to perform operations on files
#It closes the file after performing opertions

with open("C:\\Users\\namir\\OneDrive\\Documents\\Python\\Python tutorial\\ex2.txt") as e: #it is default opened in read format
    print(e.read())
print(e.closed)

with open("C:\\Users\\namir\\OneDrive\\Documents\\Python\\Python tutorial\\ex2.txt", "w") as h: #opening it in write format
    print(h.write("Hello I am doing Bachelors of Engineering\n"))
    print(h.write("In data Engineering"))

with open("C:\\Users\\namir\\OneDrive\\Documents\\Python\\Python tutorial\\ex2.txt") as e: #opening it as read format
    print(e.read()) # the text inside it will be changed a we wrote it so it erases the previous text and writes new text in write format


#writing in a file
#You can write both text and binary file
#You can either write or append in file


#Read
#using read() method we can read a file
#It opens in read formant only
#read(): reads the whole data
#read(1):reads data of lenght n
#tell(): tells you about the position of the file handle
#seek() helps to reposition of the file handle
#readliness(): reads data line by line

with open("C:\\Users\\namir\\OneDrive\\Documents\\Python\\Python tutorial\\ex2.txt") as n:
    data = n.read()
    print(data)
    print(n.read(5))
    print(n.tell())
    (n.seek(0))
    print(n.read())

 


#Handling Binary file
#To read a binary file we open the file in "rt" mode
#To write in a binary file we open file in "wt" mode 

#Append
#This mode helps us to append in a file

with open("C:\\Users\\namir\\OneDrive\\Documents\\Python\\Python tutorial\\ex2.txt", "a") as a:
    print(a.write("\nThis id appended data: In Universal college of engineering"))

with open("C:\\Users\\namir\\OneDrive\\Documents\\Python\\Python tutorial\\ex2.txt") as r:
    print(r.read())