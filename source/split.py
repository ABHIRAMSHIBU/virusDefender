a=raw_input("Enter the data to fill split1.txt:")
b=raw_input("Enter the data to fill split2.txt:")
f1=open("split1.txt","w")
f2=open("split2.txt","w")
for i in a:
	append_line=i+"\n"
	f1.write(append_line)
for i in b:
	append_line=i+"\n"
	f2.write(append_line)
f1.close()
f2.close()
