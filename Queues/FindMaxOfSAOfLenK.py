
from collections import deque
def FindMaxinSAWithKWindow(A, K):
	Q = deque()
	ANS = []
	N = len(A)
	
	for i in range(K):
		while len(Q) != 0 and A[i] >= A[Q[-1]]: ## back element
			Q.pop() ## Pop back
			
		Q.append(i) ## push back
	
	ANS.append(Q[0])
	L = 1
	R = K
	
	while R < N :
		if Q[0] == L -1 :
			Q.popleft()
		while len(Q) != 0 and A[R] >= A[Q[-1]] :
			Q.pop()
		
		Q.append(R)
		ANS.append(A[Q[0]])
		
		L += 1
		R += 1
	#return ANS
	print(f"Max in subarray of length {K} is {ANS}")


	
if __name__ == "__main__":
    A = [1 , 8, 5, 6, 7, 4, 2, 1, 9]
    K = 4
    FindMaxinSAWithKWindow(A, K)
	