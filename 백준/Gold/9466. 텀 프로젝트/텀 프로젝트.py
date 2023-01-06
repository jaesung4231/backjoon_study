import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    from_count = [0 for _ in range(n+1)]
    for num in nums:
        from_count[num] += 1

    d = deque()
    for i in range(1, n+1):
        if from_count[i] == 0:
            d.append(i)
            from_count[i] -= 1

    answer = 0
    while d:
        student = d.pop()
        answer += 1
        from_count[nums[student]] -= 1
        if from_count[nums[student]] == 0:
            d.append(nums[student])

    print(answer)