result=0

for x in range(10,1000000):
    st=str(x)

    sum=0
    for y in range(len(st)):
        num=int(st[y])
        sum+=int(num*num*num*num*num)

    if sum == int(st):
        result+=sum

print(result)
        
