from solution import sumofmultiples

def correct_sumofmultiples(L,n):
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


def test_35_1000():
	L = [3,5]
	n = 1000
	assert correct_sumofmultiples(L,n) == sumofmultiples(L,n)
	
def test_135_1000():
	L = [1,3,5]
	n = 1000
	assert correct_sumofmultiples(L,n) == sumofmultiples(L,n)

def test_2729_100000():
	L = [2,7,29]
	n = 100000
	assert correct_sumofmultiples(L,n) == sumofmultiples(L,n)