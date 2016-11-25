#convert binary to hex
import glob
from binascii import*
def binhex():
    fvirus=open("C:\\Users\\Naveen\\Desktop\\virus_test\\virus-sample.py","r").readlines()#open virus database sample
    frand=open("C:\\Users\\Naveen\\Desktop\\virus_test\\random.py","r").readlines()# open any file
    for i in range(len(fvirus)):
        fvirus[i]=fvirus[i].strip()
        if fvirus[i]=='':
            fvirus.remove(fvirus[i])
            
    #l=len(frand)    
    for j in frand:
        frand[frand.index(j)]=frand[frand.index(j)].strip()
    for i in frand:    
      if frand[frand.index(i)]=='':
        frand.remove(i)
        for k in i:
            if k=='\n':
                t=i
                t.remove(k)
                frand[index(i)]=t
            
    f1=""
    f2=""
    for i in frand:
        f1+=i
    for j in fvirus:
        f2+=j
    f1=str(f1)
    f2=str(f2)
    return f2,f1
    

def compare():
    
   testfiles=binhex()#return both virus database file and testfile
   f1=[]
   flag=0
   f2=[]
   f1=testfiles[0]
   f2=testfiles[1]
   #print f2
   #print f1
   count=0      
   s2=0  
   for s1 in range(len(f1)):
     if f1[s1] == f2[s2]:
            count+=1
            print count
            s2=f2.index(f2[s2])+1  
            if count>=5:
                flag=1
                break
            if s2>=len(f2):
                break
     else:
        count=0
        flag=0    
        
   if flag==1:
          print"infected"
   else:
        print"safezone"
compare()



    
    
    
