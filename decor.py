from time import time

def runtime(f):
	def wrapper(*arg):
		start = time()
		f(*arg)
		delta = time()-start
		print "execution time: %d seconds"%(delta)
		return time()-start
	return wrapper

def name(f):
	def wrapper(*arg):
		res = f.func_name + str(arg)
		return res
	return wrapper

@runtime
def to_low(c):
	return c.lower()

@name
def fib(n):
	if n>1:
		return fib(n-1)+fib(n-2)
	if n==1:
		return 1
	else:
		return 0

print fib(20)
