pr = open(0).read().rstrip().split('\n')
n, m = map(int, pr[0].split())

dictionary = dict(zip(pr[1:n+1], range(1, n+1)))

print('\n'.join(map(lambda x: str(dictionary[x]) if x.isalpha() else pr[int(x)], pr[n+1:])))