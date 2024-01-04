# count how many students  are fail,average marks,highest marks.
l1=[30,60,50,40,80,35,32,34,65,56,87]
l2=[]
count=0
ans='y'
while ans=='y' or ans=='n':
 for i in range(len(l1)):    
    if l1[i]<35:
        count+=1
    if 50<l1[i]<60:
       A=i+1
       l2.append(A)
    if 30<=l1[i]<35:
        l1[i]=36
 print("No of failed student:",count)
 print("Student roll is:",A)
 print("The averange marks of student is:",sum(l1)//len(l1))
 print("the highest marks of the student:",max(l1))
 print(l1)
 for j in range(5):
    Ele=int(input("Enter the student marks:"))
    l1.append(Ele)
 print(l1)
ans=input("press the y/n")     








       
