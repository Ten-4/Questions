from solution import coin_solver
#python /homes/ttp09/.local/lib/python2.7/site-packages/nose

def correct_coin_solver(coins,n):
	coins.sort()
	if n == 0:
		return 1
	if len(coins) == 0 and n != 0:
		return 0
	
	H = {  (0,1) : 1 }
	
	for num in xrange(0,n+1):
		for val in coins:
			if (num,val) not in H:
				continue
			
			for val2 in coins:
				if val2 >= val:
					if (num+val2,val2) not in H:
						H[(num+val2,val2)] = 0
					H[(num+val2,val2)] += H[(num,val)]
			
	total = 0
	for val in coins:
		if (n,val) in H:
			total += H[(n,val)]
	return total	

def test_12_4():
	coins = [1,2]
	n = 4
	assert coin_solver(coins,n) == correct_coin_solver(coins,n)

def test_125_5():
	coins = [1,2,5]
	n = 5
	assert coin_solver(coins,n) == correct_coin_solver(coins,n)

	
def test_10125_10():
	coins = [10,1,2,5]
	n = 10
	assert coin_solver(coins,n) == correct_coin_solver(coins,n)
	
def test_null_0():
	coins = []
	n = 0
	assert coin_solver(coins,n) == correct_coin_solver(coins,n)

def test_null_1():
	coins = []
	n = 1
	assert coin_solver(coins,n) == correct_coin_solver(coins,n)

def test_uk_200():
	coins = [1,2,5,10,20,50,100,200]
	n = 200
	assert coin_solver(coins,n) == correct_coin_solver(coins,n)

def test_123476526_1000():
	coins = [1,2,3,4,7,6,5,25]
	n = 1000
	assert coin_solver(coins,n) == correct_coin_solver(coins,n)	
	