class Toy():

	count = 1

	def __init__(self, name, image_url):
		self.name = name
		self.image_url = image_url
		self.id = Toy.count
		Toy.count += 1

	def __repr__(self):
		return "Toy #{}: {}".format(self.id, self.name)	