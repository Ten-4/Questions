from coins import coin_solver

def acc(L,n):
	if n < 0:
		return 0
	else:
		return L[n]

def correct_coin_solver(coins,n):
	L = [0]*(n+1)
	L[0] = 1
	for i in xrange(1,n+1):
		for i in coins:
			L[i] += acc(L,i-coins)
	return L[n]
			
			
def test_0():
	coins = [1,2,5,10,20,50,100,200]
	n = 0
	assert coin_solver(coins,n) == correct_coin_solver(coins,n)
	
def test_1_100():
	coins = [1]
	n = 100
	assert coin_solver(coins,n) == correct_coin_solver(coins,n)
	
def test_1251050100_1000():	
	coins = [1,2,5,10,50,100]
	n = 1000
	assert coin_solver(coins,n) == correct_coin_solver(coins,n)
	
def test_1237_100():	
	coins = [1,2,3,7]
	n = 100
	assert coin_solver(coins,n) == correct_coin_solver(coins,n)
	
def test_empty_10:
	coins = []
	n = 100
	assert coin_solver(coins,n) == correct_coin_solver(coins,n)
	
	
	