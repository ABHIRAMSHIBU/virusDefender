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
