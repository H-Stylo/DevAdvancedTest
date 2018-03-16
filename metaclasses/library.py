####################################################
class BaseMeta(type):

	#---------------------------------------------------
	def __new__(cls, name, bases, body):
		if not 'bar' in body:
			raise TypeError("Bar method is not defined in your derived class")
		return  super().__new__(cls, name, bases, body)


####################################################
class Base(metaclass = BaseMeta):

	#---------------------------------------------------
	def bar(self):
		return 'bar'
	
	#---------------------------------------------------
	def foo(self):
		return 'foo'