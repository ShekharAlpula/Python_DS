def quickSort(A):
	pass

def bubble_sort1(A):
	n = len(A)
	print(f"Array length is {n}")
	for i in range(0, n-1):
		print(f"Outer loop iteration {i}")
		for j in range(0, n-i-1):
			print(f"Comparing {j} and {j + 1}")
			if A[j] > A[j+1] :
				print(f"Swapping {A[j]} and {A[j+1]}")
				t = A[j]
				A[j] = A[j+1]
				A[j+1] = t
				print(f"Swapped {A[j]} and {A[j+1]}")
			else:
				print(f"No swap needed for {A[j]} and {A[j+1]}")

def bubble_sort(A):
	n = len(A)
	for i in range(0, n-1):
		for j in range(0, (n-i-1)):
			if A[j] > A[j+1] :
				A[j], A[j+1] = A[j+1], A[j]
				
if __name__ == "__main__":
	A = [64, 34, 25, 12, 22, 11, 90]
	print(f"Input array is {A}")
	bubble_sort(A)
	print(f"Sorted array is {A}")
   