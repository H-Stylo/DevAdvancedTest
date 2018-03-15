####################################################
class Poynomial:

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
		return "Poynomial(*{!r})".format(self.coeffs)

	#---------------------------------------------------
	def __add__(self, other):
		"""
		Définition de la procédure d'addition de l'objet par un équivalent
		"""
		return Poynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

	#---------------------------------------------------
	def __sub__(self, other):
		"""
		Définition de la procédure de soustration de l'objet par un équivalent
		"""
		return Poynomial(*(x - y for x, y in zip(self.coeffs, other.coeffs)))

	#---------------------------------------------------
	def __mul__(self, other):
		"""
		Définition de la procédure de multiplication de l'objet par un équivalent
		"""
		return Poynomial(*(x * y for x, y in zip(self.coeffs, other.coeffs)))

	#---------------------------------------------------
	def __truediv__(self, other):
		"""
		Définition de la procédure de division de l'objet par un équivalent
		"""
		return Poynomial(*(x / y for x, y in zip(self.coeffs, other.coeffs)))

	#---------------------------------------------------
	def __len__(self):
		"""
		Définition de la procédure de calcul de la longueur de l'objet
		"""
		return len(self.coeffs)



####################################################
if __name__ == "__main__":
	p1 = Poynomial(1, 2, 3)
	p2 = Poynomial(6, 17, 11)

	print(p1)
	print(p2)
	print(p1+p2)
	print(p1-p2)
	print(p1*p2)
	print(p1/p2)
	print(len(p1))