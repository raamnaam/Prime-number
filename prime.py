def Prime(n):
	list1 = [2,3,5,7]
	for x in xrange(11,n/2,2):
		if x%3==0 or x%5==0 or x%7==0:
			pass
		else:
			list1.append(x)
	return list1


print("Prime No.",Prime(100))
