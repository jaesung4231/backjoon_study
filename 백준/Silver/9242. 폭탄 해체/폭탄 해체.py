import sys
import heapq
input=sys.stdin.readline
word=[]
table={"******   ******": '0',"          *****":'1',"* **** * **** *": '2',
       "* * ** * ******": '3',"***    *  *****": '4',"*** ** * ** ***": '5',
       "****** * ** ***": '6',"*    *    *****": '7', "****** * ******":'8',
       "*** ** * ******":'9'}

for i in range(5):
    word.append(list(map(str,input())))

def search(x,y):
    tmp=""
    for i in range(3):
        for j in range(5):
            if y+i>=len(word[0]) or x+j>=5: return -1
            tmp+=word[x+j][y+i]
    if tmp in table:
        return table[tmp]
    else:
        return -1

cur=0
code=""
explode=False
while 1:
    if cur>=len(word[0]): break
    letter=search(0,cur)
    if letter==-1:
        explode=True
    else:
        code+=letter
    cur+=4

if int(code)%6!=0 or explode:
    print("BOOM!!")
else:
    print("BEER!!")
