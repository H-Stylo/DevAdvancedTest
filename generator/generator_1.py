from time import sleep

#---------------------------------------------------
def compute():
	"""
	Méthode n°1 : 
	Simule une requête BDD
	Résultat --> Peut importe la taille de la demande 
	 et contrairement au temps d'éxécution pouvant varier
	 l'espace mémoire alloué, lui sera toujours le même
	"""
	data = []
	for i in range(10):
		sleep(.5)
		data.append(i)
	return data

####################################################
class Compute:
	"""
	Méthode n°2 :
	Reproduction de la fonction compute() mais sous la forme de son objet ittératif
	en évitant la problèmatique du retour complet --> retourne chaque entité distinctement
	"""
	def __iter__(self):
		self.last = 0
		return self

	def __next__(self):
		if  self.last+1 >= 10:
			raise StopIteration()
		self.last += 1	
		sleep(.5)
		return self.last

#---------------------------------------------------
def compute():
	"""
	Méthode n°3 :
	Synthaxe du générateur --> reproduit le comportement de la class Compute sans
	l'inconvénient de lisibilité
	"""
	for i in range(10):
		sleep(.5)
		yield i

####################################################
if __name__ == "__main__":
	# Méthode n°1 :
	#compute()

	# Méthode n°2 :
	#for val in Compute():
	#	print(val)

	# Méthode n°3 :
	for val in compute():
		print(val)

