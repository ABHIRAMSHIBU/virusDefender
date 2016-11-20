#!/usr/bin/python2
#convert binary to hex
import glob
import binascii
import retfind
def scan_abandoned(f1,f2):
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
def scan(f1,f2):
	found=0
	count=0
	f=[]
	f2="".join(f2)
	f1="".join(f1)
	index=f2.find(f1)
	if index!=-1:
		print "WoW Infected!."
	else :
		print "Im disappointed its free from virus."
def split(a,b):
	f1=[]
	f2=[]
	for i in a:
        	f1.append(i)
	for i in b:
        	f2.append(i)
	#print "F1 \n",f1
	#print "F2 \n",f2
	return f1,f2

def binhex():
	fvirus=open("virus-sample.py","rb").read()#open virus database sample
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
retfind.retfind()
print retfind.f1
