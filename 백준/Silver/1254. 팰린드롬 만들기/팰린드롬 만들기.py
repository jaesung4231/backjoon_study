import sys
from collections import defaultdict
input=sys.stdin.readline
word=input().strip()

def check(word):
    for i in range(len(word)//2):
        if word[i]!=word[-(i+1)]:
            return False
    return True
    

if check(word):
    print(len(word))
else:
    tmp=word[:]
    for i in range(len(word)):
        new_word=tmp+word[:i][::-1]
        if check(new_word):
            print(len(new_word))
            break