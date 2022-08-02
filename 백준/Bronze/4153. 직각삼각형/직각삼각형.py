import sys
while(1):
    triangle=list(map(int,sys.stdin.readline().split()))
    triangle.sort()
    if(triangle[0]==0 and triangle[1]==0 and triangle[2]==0):
        break
    elif (triangle[0]**2)+(triangle[1]**2)==(triangle[2]**2):
        print('right')
    else:
        print('wrong')