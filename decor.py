from time import time

def runtime(f):
	def wrapper(*arg):
		start = time()
		f(*arg)
		delta = time()-start
		print "%s took %d seconds"%(f.func_name, delta)
		return time()-start
	return wrapper

def name(f):
	def wrapper(*arg):
		print f.func_name
		print str(arg)
		return f.func_name
	return wrapper

@runtime
@name
def to_low(c):
	return c.lower()

#print to_low("A")

@runtime
@name
def fib(x):
	if x>1:
		return fib(n-1)+fib(n-2)
	if x==1:
		return 1
	else:
		return 0

print fib(3)
