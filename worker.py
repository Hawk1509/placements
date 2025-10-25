def worker(arr):
	arr.sort()
	max_val=0
	i=0;j=len(arr)-1
	while(i<=j):
		if(i==j):
			current=arr[j]
		else:
			current=arr[i]+arr[j]
			max_val = max(max_val,current)
		i+=1
		j-=1
	return max_val

a=[3,5,1,2]
print(worker(a))
