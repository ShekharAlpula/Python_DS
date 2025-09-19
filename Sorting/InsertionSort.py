
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i -1 
        while j >= 0 and A[j] > key :
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    
if __name__ == "__main__" :
    A = [9, 5, 1, 4, 3]
    print(f"Input array is {A}")
    insertionSort(A)
    print(f"Sorted array is {A}")
    A = [4, 5, 12, 9, 1, 15, 6, 3, 2]
    print(f"Input array is {A}")
    insertionSort(A)
    print(f"Sorted array is {A}")