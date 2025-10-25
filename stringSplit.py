def sort_str(n):
	sorted_char = sorted(n)
	sorted_char.reverse()
	rev_str = ''.join(sorted_char)
	return rev_str

n=input().strip()
a=list(n)

print(sort_str(n))

