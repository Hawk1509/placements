#circular shift array to perform left shift on array

n=int(input())
a=[]
for i in range(n):
	x=int(input())
	a.append(x)
k=int(input("Enter num: "))
b=[]
k=k%n
b=a[k:]+a[:k]
print(b)