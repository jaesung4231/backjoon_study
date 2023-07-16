from itertools import permutations
from collections import deque, defaultdict
import sys
input=sys.stdin.readline
board=[[""]*16 for _ in range(5)]

for i in range(5):
    word=list(input().strip())
    for w in range(len(word)):
        board[i][w]=word[w]

for i in range(16):
    for j in range(5):
        if board[j][i]!="":
            print(board[j][i], end="")