# list assingment

list1=[1,2,3,4,5,6,7,8,9,10]

#list element accesing
# accesing by index

print(list1[5])

print(list1[5:])

print(list1[:5])

print(list1[1:8:2])

print(list1[8:1:-1])

print(list1[8:1:-2])

print(list1[-1:-11:-1])

print(list1[0:])

print(list1)

print(list1[::])

print(list1.index(5))


string="saurabh"
x=list(string)
print(x)


print()

#adding list
print()

listx=list1+x
print(listx)



print()
#nested list
print("nested list")
list2=[1,2,3,4,5,6,['a','b','c','d'],7,8,9,10]
print(list2)


print()
#accesing nested list element
print(list2[6])
print()
print(list2[6][3])
print()
print(list2[6][1:3])



print()

#update list

print("updating list")
print()

list1.append(11)
print(list1)


#insert element at specific position
list1.insert(1,12)
print(list1)

#removal of elemeny
list1.remove(12)
print(list1)



print()
#traversing using for loop
print("traversing using for loop")


for i in range(0,len(list1)):
    print(i)


print()

for v in list1:
    print(v)


print()

#accept user input element for list

l1=[]
n=int(input("how many ele. you wnat in list"))
for i in range(0,n):
    e=int(input("enter the ele:"))
    l1.append(e)

print(l1)
   
