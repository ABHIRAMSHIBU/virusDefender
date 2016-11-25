#!/usr/bin/python2
def retfind():
	f2=open("/home/abhiram/Python_Shit/test/encrypt.py","r").read()
	#index=0
	l=[]
	#for i in range(len(f2)):
	#	index=f2.find(index,'\n')
	#	if index==-1:
	#		break
	#	l.append(index)
	#	i=index
	#print l
	global count
	count=-1
	f1=""
	f=[]
	for i in f2:
		count=count+1
		if i=='\n':
			l.append(count)          # l is a list of positions of all \n
			continue
		f1+=i                            # f1 is the string with no \n
		f.append(i)                      # f is a list with no \n
	return f,f2,l,f1                         # Returns all shit
	

def insert():	
	f,f2,l,f1=retfind() 
	for i in range(len(f)+len(l)):           # Insert /n after disinfection        
		for j in l:
			if i==j:
				f.insert(j,'\n')
	f=''.join(f)     #to print as a string           
	return f,f2,l

f,f2,l=insert()

print f2,'\n---------------------------------------Next code --------------------------------------\n',f
print l		
