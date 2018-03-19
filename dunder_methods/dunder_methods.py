# dunder_methods.py

####################################################
class Polynomial:

	#---------------------------------------------------
	def __init__(self, *coeffs):
		"""
		Constructeur de l'objet
		"""
		self.coeffs = coeffs

	#---------------------------------------------------
	def __repr__(self):
		"""
		Surcharge de la représentation (équivalent à un toString())
		"""
		return "Polynomial(*{!r})".format(self.coeffs)

	#---------------------------------------------------
	def __add__(self, other):
		"""
		Définition de la procédure d'addition de l'objet par un équivalent
		"""
		return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

	#---------------------------------------------------
	def __sub__(self, other):
		"""
		Définition de la procédure de soustration de l'objet par un équivalent
		"""
		return Polynomial(*(x - y for x, y in zip(self.coeffs, other.coeffs)))

	#---------------------------------------------------
	def __mul__(self, other):
		"""
		Définition de la procédure de multiplication de l'objet par un équivalent
		"""
		return Polynomial(*(x * y for x, y in zip(self.coeffs, other.coeffs)))

	#---------------------------------------------------
	def __truediv__(self, other):
		"""
		Définition de la procédure de division de l'objet par un équivalent
		"""
		return Polynomial(*(x / y for x, y in zip(self.coeffs, other.coeffs)))

	#---------------------------------------------------
	def __len__(self):
		"""
		Définition de la procédure de calcul de la longueur de l'objet
		"""
		return len(self.coeffs)

	#---------------------------------------------------
	def __call__(self, index):
		"""
		Définition de la procédure d'appel après instanciation (ex : p = Polynomial --> p(1))
		"""
		return self.coeffs[index]




####################################################
if __name__ == "__main__":
	p1 = Polynomial(1, 2, 3)
	p2 = Polynomial(6, 17, 11)

	print("\n # Fonction __repr__ :")
	print(" --> {}".format(p2))

	print("\n # Fonction __add__ :")
	print(" --> {}".format(p1+p2))

	print("\n # Fonction __sub__ :")
	print(" --> {}".format(p1-p2))

	print("\n # Fonction __mul__ :")
	print(" --> {}".format(p1*p2))

	print("\n # Fonction __truediv__ :")
	print(" --> {}".format(p1/p2))

	print("\n # Fonction __len__ :")
	print(" --> {}".format(len(p1)))

	print("\n # Fonction __call__ :")
	print(" --> {}".format(p1(1)))

	print 