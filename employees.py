import random

class Employee(object):
	def __init__(self, first_name, last_name):
		self.fn = first_name
		self.ln = last_name
		

	def eat(self, food=None, companions=None):
		self.companions = companions
		self.food = food

		restaurants = ['McDonalds', 'Burger King', 'Logans Roadhouse', 'Taco Bell', 'Arbys']

		if food is None and companions is None:
			print(self.fn, "ate at", random.choice(restaurants))

		if food is not None and companions is None:
			print(self.fn, "ate a", self.food, "at the office")

		if food is None and companions is not None:
			companions = []
			print(self.fn, "and his friends", self.companions[0], self.companions[1],
				"and", self.companions[2], "ate at", random.choice(restaurants))
			
		if food is not None and companions is not None:
			companions = []
			print(self.fn, "and his friends", self.companions[0], self.companions[1], 
				"and", self.companions[2], "ate at", random.choice(restaurants), 
				"and ordered a", self.food)		


class FullTime():
  """Describes full-time employees"""
  
  def __init__(self):
    self.hours_per_week = 40

class PartTime():
  """Describes part-time employees"""

  def __init__(self):
    self.hours_per_week = 24    


class HumanResourcesEmployee(Employee, FullTime):
  """Describes human resources employees"""

  def __init__(self, first_name, last_name):
    super().__init__(first_name, last_name) # super is Employee
    FullTime.__init__(self)



class WarehouseEmployee(Employee, PartTime):
	"""Describes warehosue employees"""

	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name) # super is Employee
		PartTime.__init__(self)
