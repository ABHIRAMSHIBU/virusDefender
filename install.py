#!/usr/bin/python3
import os
def root_check():                                 # Function to determine if program runs as root
	a=os.popen('whoami').read()		  # Using whoami command
	if (a[:-1]=='root'):			  # Check with the real value
		return 1                          # Returning 1 if the user is root
	else:					  # Returning 0 is the user is any other
		return 0 # '' '' '' '' '' '' '' '' '' '' '' ''
if root_check()==1 :
	
else :
	print("You are not root! Please run this program as root.")
