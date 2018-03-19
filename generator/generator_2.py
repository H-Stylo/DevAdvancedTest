# generator_2.py

####################################################
class ApiClassic:
	"""
	Problèmatique : beaucoup d'API marche sur un système d'appels successifs
	ne marchant qu'en respectant l'ordre établi
	"""

	#---------------------------------------------------
	def __init__():
		pass

	#---------------------------------------------------
	def run_this_first():
		firstThingToDo()

	#---------------------------------------------------
	def run_this_second():
		return secondThingToDo()

	#---------------------------------------------------
	def run_this_last():
		lastThingToDo()


####################################################
class ApiWithGenerator:
	"""
	Les générateurs simplifient la démarche en forcant une suite logique 
	dans le processus évitant ainsi les erreurs d'implémentation dans l'orde
	de ces appels et ils simplifient par ailleurs la lisibilité de ces dites API
	"""

	#---------------------------------------------------
	def __init__():
		pass

	#---------------------------------------------------
	def execute_proccess()
		firstThingToDo()
		yield

		yield secondThingToDo()

		lastThingToDo()
		yield

