from solution import kbiggest

def correct_kbiggest(L,k):
	L.sort()
	L.reverse()
	if len(L) <= k-1:
		return -1
	if k <= 0:
		return -1
	return L[k-1]

def test_OOB():
	L = [4,2,3,1]
	for k in range(0,5):
		assert correct_kbiggest(L,k) == kbiggest(L,k)
