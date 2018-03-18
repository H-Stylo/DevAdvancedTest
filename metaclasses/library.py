####################################################
class BaseMeta(type):

	#---------------------------------------------------
	def __new__(cls, name, bases, body):
		if name != 'Base' and not 'bar' in body:
			raise TypeError("Bar method is not defined in your derived class")
		return  super().__new__(cls, name, bases, body)


####################################################
class Base(metaclass = BaseMeta):

	#---------------------------------------------------
	def __init_subclass__(cls, *args, **kwargs):
		print('init_subclass', args, kwargs)
		return super().__init_subclass__(cls, *args, **kwargs)
	
	#---------------------------------------------------
	def foo(self):
		return 'foo'