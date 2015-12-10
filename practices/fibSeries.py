# coding=utf-8
def fib(max):
	n1, n2 = 1, 1
	while n1 < max:
		print n1
		n1, n2 = n2, n1 + n2

if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1:
		max = int(sys.argv[1])
	else:
		max = input('List a fibonacci series up to : ')

	fib(max)
