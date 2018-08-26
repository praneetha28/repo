# Implement Merge algorithm to sort an integer array in ascending order


def merge_sort(arr,l,r):
	pass
 
 
# Driver code to test above
num = int(input())
for _ in range(num):
	user_input = input()
	list_ = user_input.split()
	arr=[]
	for i in list_:
		arr.append(int(i))
	# arr = [12, 11, 13, 5, 6, 7]
	n = len(arr)
	merge_sort(arr,0,n-1)
	print(arr)
