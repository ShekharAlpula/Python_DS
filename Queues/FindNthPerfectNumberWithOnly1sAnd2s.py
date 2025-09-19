from collections import deque

def NthPerfectNumber(n):
	Q = deque()
	cnt  = 0
	Q.append(0)
	
	while cnt < N and len(Q) != 0:
		value = Q.popleft()
		Q.append( (value * 10 ) + 1)
		Q.append( (value * 10 ) + 2)
		cnt += 1
	
	print(f"NthPerfectNumber {Q.popleft()}")

if __name__ == "__main__":
    N = 20
    NthPerfectNumber(N)

