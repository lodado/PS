sum=0 # sum is an integer variable to sum multiple of (3 or 5) below 1000

for x in range(1,1000):
    if (x%3==0 or x%5==0): # add x if x is multiple of 3 or 5 
        sum+=x

print(sum)  # print answer (233168) :) 

