# user.py

from library import Base

assert hasattr(Base, 'foo'), "Foo doesn't exist ..."

####################################################
class Derived(Base):
	
	#---------------------------------------------------
	def bar(self):
		return self.foo()

