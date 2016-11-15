#!/usr/bin/python3
# Witten by Abhiram Shibu (Team Destroyer), contibuted by so many contributers ( Abin Shoby, Abhijith N Raj, Etc )
# Licensed under GPL v2.0
import os
file= __file__
def help0():                                                                                                 # User help function declaration
	print("This program is designed to insert a particular virus file into the database")
	print("Program designed to run on python version 3")
	print("Usage "+file+" -n <virus name> -f <file name>")
	print(file+" -h, displays this message.") 
f=open("databases","a")                                                                                      # Open database file
import sys                                                                                                   # Module to use argv
import binascii as bintohex                                                                                  # Module to convert ascii to hex and bin to hex
c=0                                                                                                          # Changes Variable - declare with no changes
j=len(sys.argv)                                                                                              # Length of total arguments supplied
if (j>1):                                                                                                    # Getting rid of file name as argument
	for i in range (1,j):                                                                                # Itration so that user can enter parameters dyanmically
		if(sys.argv[i]=='-f'):                                                                       # Find -f parameter
			fname=sys.argv[i+1]                                                                  # Store file name to a variable
			c=1                                                                                  # Changes are present
		if(sys.argv[i]=='-h'):                                                                       # Find -h parameter
			help0()                                                                              # Calling for help lol
		if(sys.argv[i]=='-n'):                                                                       # Find -n parameter
			virname=sys.argv[i+1]                                                                # Store virus name to a variable
			c=1                                                                                  # Changes are present
else:                                                                                                        # Checking if no argument specified
	print("You have not given any arguments, try "+file+" -h for more details")
if (c==1):                                                                                                   # Append changes to db if changes present
	command="file -b "+fname
	linux_open=os.popen(command).read()
	if(linux_open.find("txt")==-1):
		targetextract=open(fname,"rb").read()                                                                # Read the target file
#		targetextract=targetextract.split("\n")                                                              # Removing next line
#		targetextract="".join(targetextract)                                                                 # Joining the list with a null string
		targethex=bintohex.hexlify(targetextract)                                                            # Converting to hex and storing
	else:
		targetextract=open(fname,"r").read()                                                                # Read the target file
		targetextract=targetextract.split("\n")                                                              # Removing next line
		targetextract="".join(targetextract)                                                                 # Joining the list with a null string
		targethex=bintohex.hexlify(targetextract)                                                            # Converting to hex and storing
	target_append_line="\n"+virname+"\t\t\t\t"+targethex.decode("utf-8")                                                      # Making append line in appropreate way
	f.write(target_append_line)                                                                          # Writing changes to db
f.close()                                                                                                    # Closing db
