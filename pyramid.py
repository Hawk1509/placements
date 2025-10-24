def pyramidSum(a):
	top=[]
	if len(a) == 1:
		print(a[0])
		return

	for  i in range(len(a)-1):
		topVal=a[i]+a[i+1]
		top.append(topVal)
	pyramidSum(top)
a=[]
n=int(input())
for i in range(n):
	x=int(input())
	a.append(x)
pyramidSum(a)