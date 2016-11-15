#!/usr/bin/python2
import os
a=os.popen("ls databases")
if a.read()=="":
   print "Database error Occured!"
else :
  print "Database found!"
print "End of database detection"
