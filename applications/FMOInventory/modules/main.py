numberone = 1
myage = 15

def dimehola():
	return "Hola Hendry"
	
def cuatroveces(input):
	print input * 4
	
class guitar:
	def __init__(self):
		self.type = raw_input("Favorite guitar style")
		self.height = raw_input("What height?")	
		self.price = raw_input("tell me the price")	
		self.age = raw_input("How old is it ")
		
	def printdetails(self):
		print "this guitar is a/an" + self.height + "foot",
		print self.type, "guitar, "+ self.age, "years old and costing" + self.price
