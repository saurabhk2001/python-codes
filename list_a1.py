#list
l1=[]
big=0
n=int(input("enter the list lenth:"))
for i in range(0,n):
    ele=int(input("enter the ele:"))
    l1.append(ele)
print(l1)

for i in range(len(l1)):
    if l1[i]%2==0 and big<l1[i]:
       big=l1[i]
if big==0:
    print("no enen no in list")
else:
    print("the largest enven no is:",big)
