from library import Base

assert hasattr(Base, 'foo'), "Foo doesn't exist ..."

####################################################
class Derived(Base):
	
	#---------------------------------------------------
	def barithon(self):
		return self.foo()

