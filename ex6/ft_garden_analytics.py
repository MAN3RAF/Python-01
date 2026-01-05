class Plant:
	def __init__(self, name, height):
		self.name = name
		self.height = height

	def grow(self):
		self.height += 1
		print(f"{self.name} grew 1cm")

	def get_info(self):
		print(f"- {self.name}: {self.height}cm")

class FloweringPlant(Plant):
	def __init__(self, name, height, color):
		super().__init__(name, height)
		self.color = color
		self.blooming = True

	def get_info(self):
		print(f"- {self.name}: {self.height}cm, {self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
	def __init__(self, name, height, color, points):
		super().__init__(name, height, color)
		self.points = points

	def get_info(self):
		print(f"- {self.name}: {self.height}cm, {self.color} flowers (blooming), prize points: {self.points}")


class Garden:
	def __init__(self, owner):
		self.owner = owner
		self.plants = []
		self.growth = 0

	def add_plant(self, plant):
		self.plants.append(plant)
		print(f"Added {plant.name} to {self.owner}'s garden")
	
	def grow_all(self):
		print(f"{self.owner} is helping all plants grow...")
		for plant in self.plants:
			plant.grow()
			self.growth += 1
	

class GardenManager:
	def __init__(self):
		pass
	gardens = []

	def add_garden(self, garden):
		self.gardens.append[garden]

	@classmethod
	def create_garden_network(cls):
		print(f"Total gardens managed: {len(cls.gardens)}")

	class GardenStats:
		@staticmethod
		def count_plant_types(plants):
			regular = Flowering = Prize = 0
			for plant in plants:
				if isinstance(plant, PrizeFlower):
					Prize += 1
				elif isinstance(plant, FloweringPlant):
					Flowering += 1
				else:
					regular += 1
			return regular, Flowering, Prize


print("=== Garden Management System Demo ===")

print("")

plant1 = Plant("Oak Tree", 100)
plant2 = FloweringPlant("Rose", 30, "red")
plant3 = PrizeFlower("SunFlower", 35, "yellow", 10)

garden1 = Garden("Alice")

garden1.add_plant(plant1)
garden1.add_plant(plant2)
garden1.add_plant(plant3)

print("")

list = ["SunFlower", "Rose", "Oak"]
list1 = [plant3, plant2, plant1]

alice = GardenManager

regular, Flowering, Prize = alice.GardenStats.count_plant_types(list1)

print(f"{regular} || {Flowering} || {Prize}")

print("")

GardenManager.create_garden_network()
