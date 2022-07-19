num=int(input())
total_num=[]
freq_num=[0]*9000
count=0
result=0

for i in range(num):
    input_num=int(input())
    total_num.append(input_num)
    freq_num[input_num+4500]+=1

average=sum(total_num)//num
temp=sum(total_num)/num
total_num.sort()

half_num=(temp%1)-1
if 0 > half_num >=-0.5:
    print(average+1)
else:
    print(average)

print(total_num[(num//2)])

plus_length=max(total_num)
minus_length=min(total_num)
max_freq=max(freq_num)

for i in range(minus_length+4499,plus_length+4501):
   if freq_num[i]==max_freq:
        if count==2:
            break
        result=i-4500
        count+=1

print(result)
print(plus_length-minus_length)