#to find smallest number in unsorted array

def smallest(value):
	small=value[0]
	for i in range(len(value)):
		if value[i]<small:
			small=value[i]
	print(small)

value=[56,78,45,34,99,36,98]
print("array-->",value)
smallest(value)
