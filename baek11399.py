n = int(input())
a = [int(n) for n in input().split()]
sum=0
a.sort()
for i in range(n,0,-1) :
    for j in range(i) :
        sum+=a[j]
        
print(sum)        

