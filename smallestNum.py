str1=input().strip()
print(str1)
a=list(str1)
#print(a)
a.sort()
if a[0] == '0':
	for i in range(1,len(a)):
		if (a[i] != '0'):
			a[0],a[i] = a[i],a[0]
			break
print(int(''.join(a)))