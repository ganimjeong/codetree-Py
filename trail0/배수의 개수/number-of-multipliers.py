sum3=0
sum5=0
for _ in range(10):
    n=int(input())
    if n%3==0:sum3+=1
    if n%5==0:sum5+=1
print(sum3,sum5)