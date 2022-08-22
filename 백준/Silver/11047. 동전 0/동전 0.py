import sys
N,K=map(int, sys.stdin.readline().split())
prev=1000000
coin_list=[]

for i in range(N):
    coin=int(sys.stdin.readline().strip())
    if(coin<=K):
        coin_list.append(coin)

prev=K
count=0
num=len(coin_list)

while(prev!=0):
    count+=prev//coin_list[num-1]
    prev=prev%coin_list[num-1]
    num-=1
   

print(count)
