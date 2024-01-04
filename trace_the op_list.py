#trace the o/p
#1]
l1=[1,3,5]
l1*3
>>[1, 3, 5, 1, 3, 5, 1, 3, 5]
l1*=3
l1
>>[1, 3, 5, 1, 3, 5, 1, 3, 5]
#2]
l1=["this",'is','a','list']
l2=["this",["is","another"],"list"]
a)l1==l2
>>False
c)l1[3].upper()
>>'LIST'
f)l2[1][1].upper()
>>'ANOTHER'
#4]
l1=[3,4.5,12,25.7,[2,1,0,5],88]
a)l1[3:6]
>>[25.7, [2, 1, 0, 5], 88]
b)l1[3:5]
>>[25.7, [2, 1, 0, 5]]
c)l1[4]
>>[2, 1, 0, 5]
d)l1[1:6:2]
>>[4.5, 25.7, 88]
l1[0:3]
[3, 4.5, 12]
l1[5:6]
[88]
l1[0:6]
[3, 4.5, 12, 25.7, [2, 1, 0, 5], 88]
l1[4:5]
[[2, 1, 0, 5]]
l1.pop(4)
[2, 1, 0, 5]
l1
[3, 4.5, 12, 25.7, 88]
#6]
l1=[1,3,5,7,9]
print(l1==l1.reverse())
>>False
print(l1)
>>[9, 7, 5, 3, 1]
l1.reverse()
l1
[1, 3, 5, 7, 9]
l1.reverse()
l1
[9, 7, 5, 3, 1]
#7]
my_list=['p','r','o','b','l','e','m']
my_list[2:3]
>>['o']
print(my_list)
>>['p', 'r', 'o', 'b', 'l', 'e', 'm']

my_list[2:3]=[]
print(my_list)
>>['p', 'r', 'b', 'l', 'e', 'm']
my_list[2:3]=[]
print(my_list)
>>['p', 'r', 'l', 'e', 'm']
#8]
list1=[13,18,11,16,13,18,13]
print(list1.index(18))
>>1
print(list1.count(18))
>>2
l1[4:6]

[[2, 1, 0, 5], 88]
list1.append(list1.count(13))
print(list1)
>>[13, 18, 11, 16, 13, 18, 13, 3]
#9]
odd=1,3,5
odd=[1,3,5]
print((odd+[2,4,6])[4])
>>4
print((odd+[2,4,6])[4]-(odd+[2,4,6])[4])
>>0
a,b,c=[1,2],[1,2],[1,2]
print(a is b)
>>False
print(a==b)
>>True
#11]
a)
a,b,c=[1,2],[1,2],[1,2]
print(a is b)
False
print(a==b)
True
l1,l2=[2,4],[2,4]
l3=l2
l2[1]=5
print(l3)
[2, 5]
b)
l1,l2=[2,4]
l3=list(l2)
l2[1]=5
print(l3)
>>[2, 4]
#12]
l1=[1,11,21,31]
l2=l1+2
l3=l1*2
#13]
list=['a','b','c']*-3
print(list)
>>>[]
#14]// list comprehension
data=[2,3,9]
temp=[[x for x in [data]] for x in range(3)]
print(temp)
data=[2,3,9]
temp=[x for x in[data] for x in range(3)]
print(temp)
data=[2,3,9]
temp=[x for x in data for y in range(3)]
print(temp)
>>>[[[2, 3, 9]], [[2, 3, 9]], [[2, 3, 9]]]
[0, 1, 2]
[2, 2, 2, 3, 3, 3, 9, 9, 9]
#15]
data=[x for x in range(5)]
temp=[x for x in range(7) if x in data and x%2==0]
print(temp)
>>>[0, 2, 4]
#16]
temp=['Geeks','for','Geeks']
arr=[i[0].upper() for i in temp]
print(arr)
#17]
l1=list()
l1.append([1,[2,3],4])
l1.extend([7,8,9])
print(l1[0][1][1]+l1[2])
#18]
l1=[1,1.33,'GFG',0,'NO',None,'G',True]
val1,val2=0,''
for x in l1:
    if(type(x)==int or type(x)==float):
        val1+=x
    elif(type(x)==str):
        val2+=x
    else:
        break
print(val1,val2)
#19]
l1=[1,2,3,4]
l2=l1
l3=l1.copy()
l4=list(l1)
l1[0]=[5]
print(l1,l2,l3,l4)
>>>[[5], 2, 3, 4] [[5], 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 4]

#20]
l=[1,3,5,7,9]
print(l.pop(-3),end='')
print(l.remove(l[0]),end='')
print(l)
>>>5None[3, 7, 9]
