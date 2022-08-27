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
stack=Stack()
N=int(input())
count=0
for i in range(N):
    num=int(sys.stdin.readline())
    if num:
        count+=1
        stack.push(num)
    else:
        count-=1
        stack.pop()
result=0
for i in range(count):
    result+=stack.last.item
    stack.pop()
print(result)

    