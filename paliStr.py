s=input()
x=s.split()
print(x)
l=len(x)
score=0
for word in x:
	if (word == word[::-1]):
		if (len(word) == 5):
			score+=10
		elif(len(word) == 4):
			score+=5
print(score)