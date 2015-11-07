
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


def facsum(n):
	from math import factorial
	return sum([ int(i) for i in str(factorial(n)) ])
	
def kbiggest(L,k):
	L.sort()
	L.reverse()
	if len(L) <= k-1:
		return -1
	if k <= 0:
		return -1
	else:
		return L[k-1]

def nprimes(n):
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
	
def sumofmultiples(L,n):
	total = 0
	for i in range(1,n+1):
		add = False
		for j in L:
			if i % j == 0:
				add = True
				break
		if add:
			total += i
	return total
