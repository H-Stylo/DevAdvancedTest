from time import time

#---------------------------------------------------
def timer(func):
	"""
	Décorateur caluculant le temps d'exécution d'une fonction
	"""
	def wrapper(*args, **kwargs):
		before = time()
		base_function = func(*args, **kwargs)
		after = time()
		print('elapsed : {}'.format(after - before))
		return base_function
	return wrapper

#---------------------------------------------------
def ntimes(n):
	"""
	Décorateur exécutant un nombre donné de fois une fonction
	"""
	def inner(func):
		def wrapper(*args, **kwargs):
			for i in range(n):
				print('running {} : {} times on {}'.format(func.__name__, n, i))
				base_function = func(*args, **kwargs)
			return base_function
		return wrapper
	return inner


#---------------------------------------------------
@timer
def add(x, y=1):
	return x + y

#---------------------------------------------------
@ntimes(5)
def sub(x, y=1):
	return x - y

####################################################
if __name__ == "__main__":
	print(add(5))
	print(sub(17))
