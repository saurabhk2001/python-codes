#sum of even  index of list

list1=[1,2,3,4,5,6]
sume=0
sumo=0

for i in list1:
    if i%2==0:
        sume+=i
    else:
        sumo+=i


print(sumo-sume)

