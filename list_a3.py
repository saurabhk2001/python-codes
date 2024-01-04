#list median

list1=[23,9,14,2,28,19.3,15,9,25,2,4,6]

l=len(list1)
if l%2==0:
    med=(l//2)
    median=(list1[(med-1)]+list1[med])/2
    print("median=",median)
else:
    median=int(l//2)
    print("median=",list1[median])

