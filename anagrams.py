words = input().strip().split()
count = 0 
for i in range(len(words)):
	for j in range(i+1,len(words)):
		if(sorted(words[i]) == sorted(words[j])):
 			count+=1
print(count)