n=int(input())
k=int(input())
j=int(input())
m=int(input())
p=int(input())

if n<0 or k<0 or j<0 or m<0 or p<0:
 	print("invlaid Input")
 
rem = n-(m//k+p//j)
if(m%k!=0 or p%j!=0):
	rem = rem-1
print(rem)