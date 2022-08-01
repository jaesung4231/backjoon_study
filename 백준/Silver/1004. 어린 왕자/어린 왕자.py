import sys
tc=int(input())
def find_dis( start_x, start_y, end_x, end_y):
    x_axis=(start_x-end_x)**2
    y_axis=(start_y-end_y)**2
    distan=(x_axis+y_axis)**(1/2)
    return distan

for i in range(tc):
    start_x, start_y, end_x, end_y= map(int, sys.stdin.readline().split())
    stars=[]
    star=int(input())
    count=0
    for i in range(star):
        data=(list(map(int, sys.stdin.readline().split())))
        start=find_dis(start_x,start_y,data[0],data[1])
        end= find_dis(end_x,end_y,data[0],data[1])
        if start >data[2]:
            count+=1
        if  end >data[2]:
            count+=1
        if start>data[2] and end>data[2]:
            count-=2
    print(count)