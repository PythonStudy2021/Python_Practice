#f=open("C:/doit/newFile.txt",'w')
#for i in range(1,11):
 #   data="%d line\n" % i
  #  f.write(data)
#f.close

f2=open("C:/doit/newFile.txt",'r')
for i in range(1,11):
    line=f2.readline()
    if not line:break
    print(line)
f2.close