robot_price = 900
robot_amount = 2
robot_tax = 1.25
book_price = 100
book_amount = 1
book_tax = 1.06
print(robot_price * robot_amount * robot_tax + book_price * book_tax)



robot = {"price": 900, "count": 2, "tax": 1.25}
book = {"price": 100, "count": 1, "tax": 1.06}
print(robot["price"]*robot["count"]*robot["tax"]+book["price"]*book["count"]*book["tax"])



class Product:
	price = 0
	count = 0
	tax = 1.25

robot = Product()
robot.price = 900
robot.count = 2

book = Product()
book.price = 100
book.count = 1
book.tax = 1.06

print(robot.price*robot.count*robot.tax+book.price*book.count*book.tax)
