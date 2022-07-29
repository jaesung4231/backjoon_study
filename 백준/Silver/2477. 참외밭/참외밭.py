import sys
per_size=int(input())
length=[]
direction=[]
length_up_down=[]
length_left_right=[]

for i in range(6):
    x,y=map(int,sys.stdin.readline().split())
    if(x==1 or x==2):
        length_left_right.append(y)
    else:
        length_up_down.append(y)
    length.append(y)

big_box=max(length_up_down)*max(length_left_right)
box1=length[0]*length[1]
box2=length[3]*length[4]

# print(box1, big_box)

if(box1==big_box):
    # print(1)
    result=box1-box2
    print(result*per_size)
elif(box2==big_box):
    # print(2)
    result=box2-box1
    print(result*per_size)
else:
    # print(3)
    result=box1+box2
    print(result*per_size)