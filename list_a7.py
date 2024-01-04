#m=[[1,35],[2,28],[1,58],[1,35],[1,34],[1,30],[1,75],[1,80]]

m=[23,4,56,65,38,58,69,87,90,97,30]
f=0
a=[]
ans='y'
while ans=='y':
 sum=0
 for i in range(len(m)):
    sum=sum+m[i]
    
    if m[i]<35:
        f+=1
    if 50<=m[i]<=60:
         k=i+1
         a.append(k)
    if 30<m[i]<60:
        m[i]=36
 print("total student:",len(m))
 print("total cout of fail students:",f)
 print("the rollno of students between 50 to 60 :",a)
 print("averege marks=",(sum//(len(m))))
 print("maximum marks of student roll no is ",m.index(max(m)),"marks is:",max(m))
 print("enter the next 5 students marks")
 for i in  range(5):
     ele=int(input("add marks:"))
     m.append(ele)
 ans=input("want to add more students mark: y/nS")
 print(m)
