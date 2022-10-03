import sys
input=sys.stdin.readline

arr=input().strip()
cnt=0
cnt_2=0
for i in range(len(arr)-1):
    if arr[i]=='0' and arr[i+1]=='1':
        cnt+=1
for i in range(len(arr)-1):
    if arr[i]=='1' and arr[i+1]=='0':
        cnt_2+=1
    
print(max(cnt,cnt_2),end="")
        