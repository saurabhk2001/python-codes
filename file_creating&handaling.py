#creat new file demo.txt
#1)first way

h=open('demo.txt','r')
print(h.read())
h.close()

#second way read file
with open('demo.txt','r') as h:
 print(h.read())
 h.close()
 
#2) print fiest n line(if n=5)
 
h=open('demo.txt','r')
d=h.readlines()
for i in range(5):
    print(d[i],end="  ")
h.close()

#3)append text
f=open("demo.txt","a")
f.write("line13 saurabh")
f.close()
f=open("demo.txt","r")
print(f.read())   #note: read(),readline(),readlines() try thes fun. and observ changes
f.close()

#4)read last n line(if n=5)
h=open('demo.txt','r')
d=h.readlines()
for i in range(1,5):
    print(d[-i],end="")
h.close()

5#)read line by line
h=open('demo.txt','r')
d=h.readlines()
print(d)
h.close()

#6)longest word
f=open("demo1.txt",'r')
l=0
s=f.read()
d=s.split()
for i in d:
 if len(i)>l:
     l=len(i)
     word=i
print(word)
f.close()

#7)count no of line
h=open('demo.txt','r')
d=h.readlines()
print("the count of line in file is:",len(d))
h.close()

#8) count a frequency of word
f=open("demo1.txt",'r')
s=f.read()
d=s.split()
for i in d:
  x=d.count(i)
  print(i,"count:",x)
f.close()

#9)size of file
import os
h=os.path.getsize("demo1.txt")
print(h,"bytes")

#10)write list in file
list1=['apple','banana','rohit','kajal','sonu']
f=open("demo1.txt",'w')
for i in list1:
 f.write(i)
f.close()
f=open("demo1.txt",'r')
print(f.read())
f.close()

#11)copy one to another file
with open('demo.txt','r') as f1:
    f2=open("copyfile.txt",'w')
    for i in f1:
        f2.write(f1.read())

f1.close()
f2.close()
f2=open("copyfile.txt",'r') # for read copyfile.txt
print(f2.read())
f2.close()

#12)combine lines of files

with open('demo.txt','r')as f1,open("demo1.txt","r")as f2:
 for i,j in zip(f1,f2):
    print(i+j)

f1.close()
f2.close()
#13) remove newline characters
f=open('demo.txt','r')
x=f.readlines()
print(x)
for i in x:
    print(i.rstrip())
f.close()
#14)no.of words in file
f=open('demo1.txt','r')
x=(f.read().split())
print(len(x))
f.close()
#15)extract txt file
f=open('demo1.txt','r')
print(f.readlines())
f.close()
#16) generate 26 txt file

files=[chr(x) for x in range(65,91)]
for i in files:
     with open(i+".txt","w")as f:
      f.write("the file"+i)
      f.close()
print(files)      







