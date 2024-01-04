# mode if list

list1=[1,2,3,4,53,6,2,4,2,2,2]
l1=[]
count=0
for x in list1:
 for i in range(len(list1)):
    if list1[i]==x:
        count+=1
        l1.append([x,count])
print(l1)
mx=l1[0][1]
val=l1[i][0]
for i in range(len(l1)):
    if mx<l1[i][1]:
       val=l1[i][0]
print("mode:",val)
