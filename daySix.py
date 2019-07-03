#!/usr/bin/python
import subprocess

f = open("demofile.txt",'ra+')




lines=f.readlines()

for line in lines:
    print "Line is:",line



print "Tell the current position of file"

print f.tell()

print "Set the file pointer to specific position"

f.seek(0)

print "again tell the current position of file"
print f.tell()


f.write("Writing at the end of file again2")

f1=open("AWSDeviceDefender.mkv",'r')



f2=open("/etc/hosts",'r')

allLines=f2.readlines()

for hostLine in allLines:
    firstLine=hostLine.split("\t")

    print firstLine[0]
    completed = subprocess.call('ping firstLine[0]', shell=True)
    print('returncode:', completed)



#Write a program to create a dictionary from /etc/hosts file which contain server and ip address information 
#Server name should be key and ip address should be Value 
#Write a program to read all files in a directory one by one using for loop.
#write a program to find only ip addresses from file i.e extract ip address from file.
#write a program to write into a  file at specific position 
#Write a program to  set the pointer at the mid of the file and start writing from there
#Write a program to print the string which is athe last line of file
