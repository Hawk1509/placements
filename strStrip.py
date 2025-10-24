str1 = input().strip()
str2 = input().strip()
print("str1: ",str1, "Str2 is:",str2,sep='\n')

res = ""
for i in str1:
	if i not in str2:
		res+=i
print(res)