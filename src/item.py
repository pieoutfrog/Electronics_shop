import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) >= 10:
            print("Длина наименования товара превышает 10 символов.")
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open("/home/alisa/PycharmProjects/bastards/src/items.csv", 'r', encoding='Windows-1251', newline='') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                name = row[0]
                price = row[1]
                quantity = row[2]
                cls(name, float(price), int(quantity))

    @staticmethod
    def string_to_number(number: str):
        if "." in number:
            float_number = float(number)
            int_number = int(float_number)
        else:
            int_number = int(number)
        return int_number

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        elif not isinstance(self, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        else:
            return self.quantity + other.quantity
