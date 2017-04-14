import random


class Employee(object):
	def __init__(self, first_name, last_name):
		self.fn = first_name
		self.ln = last_name

	def eat(self):
			""" eat() - Will select a random restaurant name from a list of strings, print to console that the 
			employee at at that restaurant, and also return the restaurant."""
			restaurants = ['Panera', 'Burger King', 'Logans Roadhouse', 'Taco Bell', 'Arbys']
			print(self.fn, "ate at", random.choice(restaurants))

	@overload
	def eat(food="sandwich"):
		""" eat(food="sandwich") - Will output that the employee ate that specific food at the office. """



