'''to calculate the lucky numbers in an input array'''

def Count_lucky_num(arr,num):
	count = 0
	for num in arr:
		str_num = str(num)
		for lucky in lucky_num:
			if (str_num.count(str(lucky)) == lucky):
				count+=1
				break
	return count

arr=[333,4477,347,7774]
lucky_num=[3,4,7]
print(Count_lucky_num(arr,lucky_num))


''' output: 1'''