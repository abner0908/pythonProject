#!/usr/bin/python
# codeing=UTF-8
print 'List all prime number in a given range.'

max = input('please give a upper bound: ')
for n in range(2, max):
	for factor in range(2, n):
		if n % factor == 0:
			break
	else:
		print n, 'is a prime number'