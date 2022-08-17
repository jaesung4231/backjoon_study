import sys
while(1):
    first_num, sec_num=map(int, sys.stdin.readline().split())
    if(first_num==0 and sec_num==0):
        break
    if(sec_num>first_num):
        if(sec_num%first_num==0):
            print("factor")
        else:
            print("neither")
    elif(first_num>sec_num):
        if(first_num%sec_num==0):
            print("multiple")
        else:
            print("neither")


