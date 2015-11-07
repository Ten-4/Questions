from solution import coin_solver

def correct_coin_solver(coins,n):
	coins.sort()
	if n == 0:
		return 1
	if len(coins) == 0 and n != 0:
		return 0
	
	H[ (0,0) ] = 1
	for num in range(1,n+1):
		for lcoin in coins:
			H[(num,lcoin)] = 0
			
			for val in coins:
				if val >= lcoin and (num,lcoin-val) in H:
					H[(num,lcoin)] += H[(num,lcoin-val)]
	total = 0
	for val in coins:
		if (n,val) in H:
			total += H[(n,val)]
	return total
	
def test_empty0():
	coins = []
	n = 0
	print correct_coin_solver(coins,n)
	assert coin_solver(coins,n) == correct_coin_solver(coins,n)

def test_empty1():
	coins = []
	n = 1
	print correct_coin_solver(coins,n)
	assert coin_solver(coins,n) == correct_coin_solver(coins,n)

	
def test_uk0():
	coins = [1,2,5,10,20,50,100,200]
	n = 0
	print correct_coin_solver(coins,n)
	assert coin_solver(coins,n) == correct_coin_solver(coins,n)
	
def test_uk200	
	coins = [1,2,5,10,20,50,100,200]
	n = 200
	print correct_coin_solver(coins,n)
	assert coin_solver(coins,n) == correct_coin_solver(coins,n)
	
	