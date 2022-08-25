import sys
N=int(input())
price=0
distance=list(map(int, sys.stdin.readline().split()))
city=list(map(int, sys.stdin.readline().split()))
current_price=city[0]
for i in range(len(city)-1):
    if city[i]<current_price:
       current_price=city[i]
    price+=(current_price*distance[i])
print(price)