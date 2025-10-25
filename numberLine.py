def farthest_pt(arr):
	pos=0
	max_dist=0
	for i,val in enumerate(arr):
		if i%2==0:
			pos+=val
		else:
			pos-=val
		max_dist=max(max_dist,abs(pos))
	return max_dist

a=[1,2,3,4,5]
print(farthest_pt(a))