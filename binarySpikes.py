n=int(input())
l=list(map(int,input().split()))
s=int(input())
p=[]
for i in l:
  b=bin(i)
  t=b[2:]
  if len(t)>s:
    f=t[:-s]
    p.append(int(f,2))
  else:
    p.append(0)
print(*p)