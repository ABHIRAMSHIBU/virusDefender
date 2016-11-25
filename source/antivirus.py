#!/usr/bin/python2
#NO T.I.M.E so breief commending
#convert binary to hex
import glob                # useless, for developer purpose
import binascii            # u know it , hex - dec - ascii - bin
def scan_abandoned(f1,f2):       # abandoned no need to know
	found=0
	count=0
	for i in range(len(f1)):
		temp=i	
		k=1		
		if found==1:
			break
		else :
			count=0
		for j in range(len(f2)) :
			if f1[i]==j:
				count+=1
				if k in range(20):
					if f1[temp+k]==f2[j+k]:
						count+=1
					if count==20:
						found=1
						print "Infected Be scared! BOOM!"
#				if i<len(f1):
#					i+=1
				print count
			else:
				count=0
			if count==20:
				print "Infected Be scared! BOOM!"
				found=1
				break
def scan(f1,f2):                          # New can definition
	found=0                           # flag as found
	count=0                           # To keep track of counter
	f=[]
	f2="".join(f2)                    # List -> string
	f1="".join(f1)                    # Same again
	index=f2.find(f1)                 # Finding the signature
	if index!=-1:                     # Checking if infected!
		print "WoW Infected!."    # alert user
	else :                            # if not infected
		print "Im disappointed its free from virus." # you know it
def split(a,b):                           # Split function, string -> list
	f1=[]                             # Initialize empty variable as a list
	f2=[]                             # Initialze again 
	for i in a:                       
        	f1.append(i)              # Append into f1
	for i in b:
        	f2.append(i)
	#print "F1 \n",f1
	#print "F2 \n",f2
	return f1,f2

def binhex():
	fvirus=open("databases","rb").readline()#open virus database sample
	frand=open(raw_input("Enter the name of the file to compare :"),"rb").read()# open any file
	fvirus=fvirus.split("\n")#remove newline
	fvirus="".join(fvirus)
	frand=frand.split("\n")#""
	frand="".join(frand)
	fvirus=binascii.hexlify(fvirus)#convert binary to hex
	frand=binascii.hexlify(frand)#" "   
	#print"virus sample",fvirus
	#print"file:",frand
	return(split(fvirus,frand))

f1,f2=binhex()
#print "F1 \n",f1                    # Uncommend for debugging
#print "F2 \n",f2                    # Uncommend for debugging
scan(f1,f2)

def filter(f1,f2):
	f2="".join(f2)
	f1="".join(f1)
	index=f2.find(f1)
	x=len(f2)-index+2
	f=f2[:x]
	return f



import io
f=io.FileIO("cleancode.txt","w")





neat=filter(f1,f2)
#f.open('cleancode.py','w+')
f.write(binascii.unhexlify(neat))
f.close()		


