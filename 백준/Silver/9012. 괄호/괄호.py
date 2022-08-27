import sys
class Node: 
    def __init__(self, item, next):
        self.item=item
        self.next=next
class Stack:
    def __init__(self):
        self.last=None
    def push(self, item):
        self.last=Node(item, self.last)
    def pop(self):
        if self.last:
            item=self.last.item
            self.last=self.last.next
            return item
        else:
            return(-1)

table={
    ')':'(',
    '}':'{',
    ']':'[',
}

N=int(input())
stack=[]
for k in range(N):
    line=sys.stdin.readline().strip()
    stack=[]
    for i in range(len(line)):
        if line[i] not in table:
            stack.append(line[i])    
        elif (not stack) or (table[line[i]]!=stack.pop()):
            print('NO')
            break
        if (i==(len(line)-1)) and len(stack)!=0:
            print('NO')
            break
        elif i==(len(line)-1):
            print('YES')
        