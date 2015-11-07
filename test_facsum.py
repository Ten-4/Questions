from solution import facsum
#python /homes/ttp09/.local/lib/python2.7/site-packages/nose

from math import factorial
def correct_facsum(n):
	return sum([ int(i) for i in str(factorial(n)) ])
	

def test_0():
	n = 0
	assert facsum(n) == correct_facsum(n)

def test_1to40():
	for n in range(0,40):
		assert facsum(n) == correct_facsum(n)