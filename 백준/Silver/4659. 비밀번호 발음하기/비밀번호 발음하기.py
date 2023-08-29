import sys
from collections import deque
input=sys.stdin.readline
vowel={'a','e','i','o','u'}
eo={'e','o'}

def check(word):
    inside=False
    for w in word:
        if w in vowel:
            inside=True
            break
    if not inside:
        return False
    
    for i in range(len(word)-2):
        if word[i] in vowel and word[i+1] in vowel and word[i+2] in vowel:
            return False
        elif word[i] not in vowel and word[i+1] not in vowel and word[i+2] not in vowel:
            return False
    
    for i in range(len(word)-1):
        if word[i]==word[i+1] and word[i] not in eo:
            return False
    return True
    

while 1:
    password=input().strip()
    if password =="end": break
    if check(password):
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
