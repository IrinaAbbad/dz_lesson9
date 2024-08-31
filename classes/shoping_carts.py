# 3. Класс для управления корзиной покупок

class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    Которая позволяет добавлять и удалять товары, а также подсчитывать общую стоимость товаров в корзине.
    """

    # Конструктор класса, который инициализирует пустой список items, куда будут добавляться товары, которые пользователь поместил в корзину
    def __init__(self, customer, admin): 
        self.items = []
        self.customer = customer
        self.admin = admin

    def add_item(self, product, quantity):
        """
        Добавляет продукт в корзину.
        Метод добавляет словарь с ключами "Продукт" и "количество" в список items
        """
        self.items.append({"Продукт": product, "количество": quantity})

    def remove_item(self, product_name):
        """
        Удаляет из списка items все товары, у которых имя совпадает с product_name
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]

    def get_total(self):
        """
        Возвращает общую стоимость продуктов в корзине.
        Проходит по каждому элементу в items и суммирует произведения цены (item["Продукт"].price) на количество (item["количество"]).
        """
        total = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total

    def get_details(self):
        """
        Возвращает детализированную информацию о содержимом корзины и общей стоимости.
        Метод создает строку с описанием содержимого корзины и общей стоимостью.
        Проходит по каждому элементу в items и добавляет к строке информацию о продукте
        используя метод get_details() у объекта Продукт) и его количестве.
        Добавляет общую стоимость в конце.
        """
        details = f"{self.customer.get_details()}\nприобрел: \n"
        for item in self.items:
            details += f"{item['Продукт'].get_details()}, Количество: {item['количество']}\n"
        details += f"Общая сумма покупок: {self.get_total()} руб\n"
        details += f"Зарегистрировал покупки: {self.admin.get_details()}"
        return details