from classes.products import Electronics, Clothing, Furniture
from classes.users import Customer, Admin
from classes.shoping_carts import ShoppingCart


# Создаем продукты
laptop = Electronics(name="Ноутбук", price=120000, brand="Dell", warranty_period=2)
tshirt = Clothing(name="Футболка", price=200, size="M", material="Хлопок")
table = Furniture(name="Стол", price=20000, material="Стекло", style="Модерн")

# Создаем пользователей
customer = Customer(username="Мария", email="maria@gmail.com", address="Moscow")
admin = Admin(username="root", email="root@derkunov.ru", admin_level=5)

# Создание корзины покупок
cart = ShoppingCart(customer=customer, admin=admin)

# Создаем корзину покупок и добавляем товары
cart.add_item(laptop, 1)
cart.add_item(tshirt, 3)
cart.add_item(table, 1)

# Выводим детали корзины
print(cart.get_details())
