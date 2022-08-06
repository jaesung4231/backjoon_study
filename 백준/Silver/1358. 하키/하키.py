import sys
W,H,X,Y,P= map(int, sys.stdin.readline().split())
play=0
R=H/2
area_X=(X-R,X+W+R)
area_Y=(Y, Y+H)
for i in range(P):
    x,y=map(int, sys.stdin.readline().split())
    if(x >= area_X[0] and x <= area_X[1]):
        if(y >= area_Y[0] and y <= area_Y[1]):
            if(x<X):
                dis= (((x-X)**2)+((y-(Y+R))**2))**(1/2)
                if(dis>R):
                  play-=1
            elif(x>(X+W)):
                dis= (((x-(X+W))**2)+((y-(Y+R))**2))**(1/2)
                if(dis>R):
                  play-=1
            play+=1
      
print(play)