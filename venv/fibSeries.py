# coding=utf-8
def fib(max):
	n1, n2 = 1, 1
	while n1 < max:
		print n1
		n1, n2 = n2, n1 + n2

max = input('List a fibonacci series up to : ')
fib(max)
