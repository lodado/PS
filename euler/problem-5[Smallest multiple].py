def GCD(a,b):  #Great Common Divisor
    return GCD(b,a%b) if b else a

smallest_positive_number = 1 # we start from 1 to 20
num=1

while num<=20: #multiple with a non common number=(num/greatest common divisor)
    smallest_positive_number *= num/GCD(smallest_positive_number,num)
    num+=1

print(smallest_positive_number) #print answer(232792560) :)
