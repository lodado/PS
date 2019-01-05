sum=1
for x in range(1,101):
    sum*=x

sumstr=str(sum)
result=0
for x in range(len(sumstr)):
    result+=int(sumstr[x])

print(result)
