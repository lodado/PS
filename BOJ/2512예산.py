import sys
import math

N = int(sys.stdin.readline())

province = []
province = sorted(list(map(int, list(sys.stdin.readline().split()))))
total = int(sys.stdin.readline())

maxi = 0

low = 0  
high = province[-1]

while(low<=high):
    mid = (low + high)//2
    totalcost = sum(list(map(lambda x: x if x<=mid else mid, province)))
    if(totalcost>total):
        high = mid-1
    else:
        low = mid+1

print(high)
