def repeatingAndMissingElement(arr):
	n = len(arr)
	sumArr = sum(arr)
	sumEle = sum([i for i in range(0,n+1)])
	print("Missing element: ",sumArr-sumEle)	
	setEle = set(arr)
	sumSet = sum(setEle)
	print("Repeating element: ",sumArr-sumSet)

repeatingAndMissingElement([1,2,4,5,6,6])