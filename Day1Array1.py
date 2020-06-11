def findDuplicates(arr):
	dict = {}
	n = len(arr)
	for i in range(n):
		if arr[i] in dict.keys():
			dict[arr[i]] += 1
		else:
			dict[arr[i]] = 1 

	for i in dict:
		print(i,dict[i])


findDuplicates([0,0,1,1,2,3,1])
