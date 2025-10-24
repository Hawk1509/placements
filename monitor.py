n=int(input())
a=[int(x) for x in input().split()]
print(a)
i=0
count = 0;q=a[0]
for i in range(n):
	if q > a[i]:
		count += 1
print(count)
