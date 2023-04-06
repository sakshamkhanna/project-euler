N=1000

s = sum(i for i in range(N) if not i%3 or not i%5)
print(s)