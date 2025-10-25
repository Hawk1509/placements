def max_diff(arr):
	arr.sort()
	max_val = 0;val=0
	if len(arr)<2:
		return 0
	for i in range(len(arr)-1):
		val = arr[i+1] - arr[i]
		max_val = max(max_val,val)
	return max_val

a=list(map(int,input().split()))
print(max_diff(a))
