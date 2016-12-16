#!/usr/bin/python2
import sys
import os
if len(sys.argv)==1 :
	print "Sorry this file is only for developers and maintainers."
        print __file__+" -n virusName -s sigNature"
else :
	for i in range(1,len(sys.argv)+1):
		if sys.argv[i]=='-n' :
			name=sys.argv[i+1]
		if sys.argv[i]=='-s' :
			sig=sys.arg[i+1]
append_line=name+'!0x1ebf'+sig+'\n'
f.open('databases','a')
f.write(append_line)
