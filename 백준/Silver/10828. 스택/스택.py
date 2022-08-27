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
            print(item)
            return item
        else:
            print(-1)
    def top(self):
        if self.last:
            print(self.last.item)
        else:
            print(-1)
    def empty(self):
        if self.last:
            print(0)
        else:
            print(1)
stack=Stack()
count=0
N=int(input())
for i in range(N):
    func=((sys.stdin.readline().split()))
    if 'push' in func:
        stack.push(func[1])
        count+=1
    elif 'pop' in func:
        stack.pop()
        if count>0:
            count-=1
        else:
            count=0
    elif 'top' in func:
       stack.top()
    elif 'empty' in func:
        stack.empty()
    elif 'size' in func:
        print(count)



    