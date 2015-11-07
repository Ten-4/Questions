
def coin_solver(coins,n):
	if len(coins) == 0:
		return -1
	
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