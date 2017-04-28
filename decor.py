from time import time

def runtime(f):
	def wrapper(*arg):
		start = time()
		f(*arg)
		delta = time()-start
		print "execution time: %d seconds"%(f.func_name, arg, delta)
		return time()-start
	return wrapper

def name(f):
	def wrapper(*arg):
		ret = f(*arg)
		res = "%s%s"%(f.func_name, arg)
		print res
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

print fib(5)
