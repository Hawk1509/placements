''' remove the string having '10' and '11' and print the len of the new string'''
n=input().strip()
n=n.replace('10','').replace('11','')
print(len(n))