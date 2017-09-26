# Variables
robot_price = 900
robot_amount = 2
robot_tax = 1.25
book_price = 100
book_amount = 1
book_tax = 1.06
print(robot_price * robot_amount * robot_tax + book_price * book_tax)

# Dictionary
robot = {"price": 900, "count": 2, "tax": 1.25}
book = {"price": 100, "count": 1, "tax": 1.06}
print(robot["price"]*robot["count"]*robot["tax"]+book["price"]*book["count"]*book["tax"])


# # Class
# class Product:
# 	price = 0
# 	count = 0
# 	tax = 1.25

# robot = Product()
# robot.price = 900
# robot.count = 2

# book = Product()
# book.price = 100
# book.count = 1
# book.tax = 1.06

# print(robot.price*robot.count*robot.tax+book.price*book.count*book.tax)

# Class + method
# class Product:
# 	price = 0
# 	count = 0
# 	tax = 1.25

# 	def price_with_tax(self):
# 		return self.price * self.count * self.tax

# robot = Product()
# robot.price = 900
# robot.count = 2

# book = Product()
# book.price = 100
# book.count = 1
# book.tax = 1.06

# print(robot.price_with_tax()+book.price_with_tax())

# class Product:
# 	def price_with_tax(self):
# 		return self.price * self.count * self.tax

# 	def __init__(self, price, count, tax):
# 		self.price = price
# 		self.count = count
# 		self.tax = tax

# robot = Product(price=900, count=2, tax=1.25)
# book = Product(price=100, count=1, tax=1.06)


# print(robot.price_with_tax()+book.price_with_tax())


# products = [Product(price=900,count=2, tax=1.25), Product(price=100, count=1, tax=1.06)]
# total_price = products[0].price_with_tax() + products[1].price_with_tax()
# print(total_price)

# products = [Product(price=900,count=2, tax=1.25), Product(price=100, count=1, tax=1.06)]
# total_price = 0
# for product in products:
# 	total_price = total_price + product.price_with_tax()
# print(total_price)




class Product:
	def price_before_tax(self):
		return self.price * self.count

	def __init__(self, price, count, category):
		self.price = price
		self.count = count
		self.category = category

	def tax(self):
		if self.category=="book":
			return 1.06
		else:
			return 1.25

		

products = [Product(price=900,count=2, category="robot"), Product(price=100, count=1, category="book")]

total_price = 0
for product in products:
	total_price = total_price + product.price_before_tax() * product.tax()

print(total_price)









