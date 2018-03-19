# context_manager.py

from sqlite3 import connect
from contextlib import contextmanager

#---------------------------------------------------
def classicContextManager():
	"""
	Utilsation classique d'un context manager dans le cadre de l'ouverture d'une connexion
	ou plus généralement l'ouverture d'un fichier
	"""
	with connect('context_manager.db') as conn:	
		cur = conn.cursor()

		cur.execute('create table points(x int, y int)')

		cur.execute('insert into points(x, y) values (4, 1)')
		cur.execute('insert into points(x, y) values (2, 3)')
		cur.execute('insert into points(x, y) values (1, 1)')

		for row in cur.execute('select x, y from points'):
			print(row)

		for row in cur.execute('select sum(x * y) from points'):
			print(row)

		cur.execute('drop table points')


#---------------------------------------------------
@contextmanager
def tempTableGenerator(cur):
	"""
	Genérateur du context manager permettant de forcer l'ordre du processus de 
	création et de suppression de la table
	"""
	print("created table")
	cur.execute('create table points(x int, y int)')
	try:
		yield
	finally:
		print("dropped table")
		cur.execute('drop table points')


####################################################
class TempTable:
	"""
	Création d'une personalisation d'un context manager pour répondre plus facilement 
	à la problèmatique de la fonction classicContextManager()
	"""

	#---------------------------------------------------
	def __init__(self, gen):
		self.gen = gen
	
	#---------------------------------------------------
	def __call__(self, *args, **kwargs):
		self.args, self.kwargs = args, kwargs
		return self

	#---------------------------------------------------
	def __enter__(self):
		self.gen_inst = self.gen(*self.args, **self.kwargs)
		next(self.gen_inst)

	#---------------------------------------------------
	def __exit__(self, *args):
		next(self.gen_inst, None)

#---------------------------------------------------
def personalisationContextManager():
	"""
	Utilsation du context manager personalisé pour supprimer le besoin de création 
	et suppression de la table au sein du code métier
	"""
	with connect('context_manager.db') as conn:
		cur = conn.cursor()

	#	with TempTable(tempTableGenerator)(cur): 			# Utilisation de TempTable : pas très esthétique
															# et lourd à l'écriture du context context_manager
															# --> simplification grace à contextlib possèdant un
															# décorateur transformant un decorateur en contextmanager
		with tempTableGenerator(cur):
			cur.execute('insert into points(x, y) values (4, 1)')
			cur.execute('insert into points(x, y) values (2, 3)')
			cur.execute('insert into points(x, y) values (1, 1)')

			for row in cur.execute('select x, y from points'):
				print(row)

			for row in cur.execute('select sum(x * y) from points'):
				print(row)


####################################################
if __name__ == "__main__":
	personalisationContextManager()