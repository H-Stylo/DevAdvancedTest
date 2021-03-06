# decorator_methods_1.py

#---------------------------------------------------
def controler_types(*a_args, **a_kwargs):
    """
    On attend en paramètres du décorateur les types souhaités. On accepte
    une liste de paramètres indéterminés, étant donné que notre fonction
    définie pourra être appelée avec un nombre variable de paramètres et que
    chacun doit être contrôlé
    """
    
    def decorateur(fonction_a_executer):
        """
        Notre décorateur. Il doit renvoyer fonction_modifiee
        """
        def fonction_modifiee(*args, **kwargs):
            """
            Notre fonction modifiée. Elle se charge de contrôler
            les types qu'on lui passe en paramètres"""
            
            if len(a_args) != len(args):
                raise TypeError("le nombre d'arguments attendu n'est pas égal au nombre reçu")
            # On parcourt la liste des arguments reçus et non nommés
            for i, arg in enumerate(args):
                if a_args[i] is not type(args[i]):
                    raise TypeError("l'argument {0} n'est pas du type {1}".format(i, a_args[i]))
            
            # On parcourt à présent la liste des paramètres reçus et nommés
            for cle in kwargs:
                if cle not in a_kwargs:
                    raise TypeError("l'argument {0} n'a aucun type précisé".format(repr(cle)))
                if a_kwargs[cle] is not type(kwargs[cle]):
                    raise TypeError("l'argument {0} n'est pas de type{1}".format(repr(cle), a_kwargs[cle]))
            return fonction_a_executer(*args, **kwargs)
        return fonction_modifiee
    return decorateur

#---------------------------------------------------
def controleType(decoratedFunction):
	def decorator(*args):
		print("Je vais modifier le comportement de la function ...")
		return decoratedFunction(*args)
	return decorator


####################################################
class DecoratorTest(object):
	"""
	Classe de test des decorateurs
	"""

	#---------------------------------------------------
	def __new__(cls):
		return object.__new__(cls)

	#---------------------------------------------------
	def __init__(self):
		pass
	
	#---------------------------------------------------
	@controleType
	def generateSimpleTable(self, nbRep):
		"""
		Retourne une table d'entiers
		:param nbRep: [int] taille du tableau à créer 
		"""
		return range(nbRep)

	#---------------------------------------------------
	@staticmethod
	@controler_types(int)
	@controleType
	def showNumber(myNum):
		"""
		Affiche un nombre
		:param myNum: [int] 
		"""
		print("Le nombre est : {}".format(myNum))
	

####################################################
if __name__ == "__main__":
	decoratorTest = DecoratorTest()

	decoratorTest.showNumber(2)

	sequence = [str(n) for n in decoratorTest.generateSimpleTable(10)]
	print(sequence)

	 


