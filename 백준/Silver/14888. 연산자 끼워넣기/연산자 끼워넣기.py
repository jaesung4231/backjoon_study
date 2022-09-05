from itertools import permutations
import sys
N=int(input())
number=list(map(int,sys.stdin.readline().split()))
func=list(map(int,sys.stdin.readline().split()))

def calculate(func,x,y):
    if func=='+':
        return x+y
    elif func=='-':
        return x-y
    elif func =='*':
        return x*y
    elif func =='/':
        if x<0 and y>0:
            tmp=(-x)
            return -(tmp//y)
        else:
            return x//y
string=[]
for i in range(func[0]):
    string.append('+')
for i in range(func[1]):
    string.append('-')
for i in range(func[2]):
    string.append('*')
for i in range(func[3]):
    string.append('/')

data=sorted(set(permutations(string,len(string))))
result=[]
for i in range(len(data)):
    temp=number[0]
    for j in range(len(number)-1):
        temp=calculate(data[i][j],temp,number[j+1])
    result.append(temp)
print(max(result))
print(min(result), end=" ")