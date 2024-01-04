
sack=[2,3,4,6,8,2,1,3,2,1,4,1,5,1]
n=len(sack)
print("the no of road in th sack:",n)
a_sum=0
b_sum=0
for i in range(0,n):
    if i%2==0:
        max(sack)
        
            a_sum+=sack[i]
            if a_sum!=1:
                y=a_sum/2
                a_sum=a_sum+(y)
                sack.append(a_sum)
        else:
            b_sum+=sack[i]
            if b_sum!=1:
                y=b_sum/2
                b_sum=b_sum+(y)
                sack.append(b_sum)
            
print(a_sum)
print(b_sum)
