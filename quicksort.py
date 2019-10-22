def partition(arr, start, end):
	# follower & leader start at the leftt of the list
	follower = leader = start
	# leader is a loop counter.  It increments until it hits the pivot
	# follower keeps count of swap operations, 
	# which also counts where the pivot should end up
	while leader < end:
		#  if leader is smaller than pivot, push it to the left
		if arr[leader] <= arr[end]:
			arr[follower], arr[leader] = arr[leader], arr[follower]
			follower += 1
		leader += 1
	# swap follower and end
	arr[follower], arr[end] = arr[end], arr[follower]
	# returns index
	return follower

def quicksortHelper(arr, start, end):
	if start >= end:
		return
	p = partition(arr, start, end)
	# sort left side
	quicksortHelper(arr, start, p-1)
	# sort right side
	quicksortHelper(arr, p+1, end)
	

def quicksort(arr):
	quicksortHelper(arr, 0, len(arr)-1)

import random

list = [random.randrange(10000) for i in range(100000)]

quicksort(list)
print(list)

# https://www.codementor.io/garethdwyer/quicksort-tutorial-python-implementation-with-line-by-line-explanation-p9h7jd3r6