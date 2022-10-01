import sys
input=sys.stdin.readline
N=int(input())
max_price=0
answer=0
for i in range(N):
    num=int(input())
    price=list(map(int,input().split()))  
    length=len(price)
    max_price=price[length-1]
    answer=0
    for i in range(length-1,-1,-1):
        if price[i]>=max_price:
            max_price=price[i]
        else:
            answer+=(max_price-price[i])
        
    print(answer)

      