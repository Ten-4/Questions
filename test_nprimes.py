from solution import nprimes

def correct_nprimes(n):
	if n < 2:
		return 0
	
	L = [0]*(n+1)
	L[0] = 1
	L[1] = 1
	for i in range(2,n+1):
		if L[i] == 0:
			for j in range(2,n/i+1):
				L[i*j] = 1
	return n-sum(L)+1
	

def test_neg():
	assert nprimes(-1) == 0

def test_10():
	assert nprimes(10) == correct_nprimes(10)
	
def test_100000():
	assert nprimes(100000) == correct_nprimes(100000)