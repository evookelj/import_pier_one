from time import time

def runtime(f):
	def wrapper(*arg):
		start = time()
		f(*arg)
		delta = time()-start
		print "%s took %d seconds"%(f.func_name, delta)
		return time()-start
	return wrapper

@runtime
def to_low(c):
	return c.lower()

print to_low("A")