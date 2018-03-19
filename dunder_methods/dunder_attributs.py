# dunder_attributs.py

from inspect import getsource, getfile

####################################################
def add(x, y=1):
	return x + y

####################################################
if __name__ == "__main__":
	print("\n # Attributs __name__ :")
	print(" --> {}".format(add.__name__))

	print("\n # Attributs __defaults__ :")
	print(" --> {}".format(add.__defaults__))

	print("\n # Attributs __code__.co_code :")
	print(" --> {}".format(add.__code__.co_code))

	print("\n # Attributs __code__.co_varnames :")
	print(" --> {}".format(add.__code__.co_varnames))

	print("\n # Source code with Inspect library :")
	print(" --> {}".format(getsource(add)))

	print("\n # File code with Inspect library :")
	print(" --> {}".format(getfile(add)))