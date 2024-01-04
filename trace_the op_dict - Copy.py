#Trace the o/p Dictionary
#1]
t=(1,2,3,4,5,6,7,8)
print(t[t.index(5)])
print(t[t[t[6]-3]-6])
>>>5
8
#2]
t1=(1)
t2=(3,4)
t1+=5
print(t1)
print(t1+t2)
>>>6
#3]
dictionary={'GFG':'geeksforgeeks.org','google':'google.com','facebook':'facebook.com'}
del dictionary['google']
for key,values in dictionary.items():
    print(key)
>>>GFG
facebook
#4]
dictionary1={'Google':1,'Facebook':2,'Microsoft':3}
dictionary2={'GFG':1,'Microsoft':2,'Youtube':3}
dictionary1.update(dictionary2)
for key,values in dictionary1.items():
    print(key,values)
>>>Google 1
Facebook 2
Microsoft 2
GFG 1
Youtube 3
#5]
dictionary1={'GFG':1,'Google':2,'GFG':3}
print(dictionary1['GFG'])
>>>3
#6]
temp={'GFG':1,'Facebook':2,'Google':3}
for(key,values)in temp.items():
    print(key,values,end='')
>>>GFG 1Facebook 2Google 3
#7]
dictionary={}
dictionary[1]=1
dictionary['1']=2
dictionary[1]+=1
dictionary={1:3}
sum=0
for k in dictionary:
    sum+=dictionary[k]
print(sum)
>>>3
#8]
dictionary={1:'1',2:'2',3:'3'}
del dictionary[1]
dictionary[1]='10'
del dictionary[2]
print (len( dictionary))
>>>2
#9]
d={1:[1,2,3,4],2:(4,6,8)}
d[1].append(4)
print(d[1],end='')

l=list(d[2])
l.append(10)
d[2]=tuple(l)
print(d[2])
>>>[1, 2, 3, 4, 4](4, 6, 8, 10)
#10]
var1='Hello Geeks!'
var2="GeeksforGeeks"
print("var1[0]:",var1[0])
print("var2[1:5]:",var2[1:5])
>>>var1[0]: H
var2[1:5]: eeks
#11]
var1='Geeks'
print("Original String:-",var1)
print("updated string:-",var1[:5]+'for'+'Geeks')
>>>Original String:- Geeks
updated string:- GeeksforGeeks
#12]
list=[True,50,10]
list.insert(2,5)
print(list,"Sum is:",sum(list))
>>>[True, 50, 5, 10] Sum is: 66
#14]
l=[1,3,5,7,9]
print(l.pop(-3),end='')
print(l.remove(l[0]),end='')
print(l)
>>>5None[3, 7, 9]
#15]
temp=dict()
temp['key1']={'key1':44,'key2':566}
temp['key2']=[1,2,3,4]
for(key,values)in temp.items():
    print(values,end="")
>>>{'key1': 44, 'key2': 566}[1, 2, 3, 4]
    

    
