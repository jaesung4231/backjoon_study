import sys
A,B=sys.stdin.readline().split()
A_set=set()
B_set=set()
A_set.update(list(map(int,sys.stdin.readline().split())))
B_set.update(list(map(int,sys.stdin.readline().split())))
tmp_1=A_set-B_set
tmp_2=B_set-A_set
print(len(tmp_1)+len(tmp_2))
