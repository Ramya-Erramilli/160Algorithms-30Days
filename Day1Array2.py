def sort012_inPlace(a):
	low,mid,high = 0,0,len(a)-1
	while(mid<=high):
		if a[mid]==0:
			a[low],a[mid] = a[mid],a[low]
			low = low+1
			mid = mid+1
		elif a[mid]==1:
			mid = mid+1
		else:
			a[mid],a[high] = a[high],a[mid]
			high = high-1

	print(a)

sort012_inPlace([0,0,1,2,1,0,1,2,1])
