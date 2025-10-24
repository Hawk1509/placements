n=int(input())
a=[int(x) for x in input().split()]
print(a)
i=n
count = 0
while(i != 0):
	if a[i] < a[i-1]:
		count = count+1
	i=i-1
print(count) 

