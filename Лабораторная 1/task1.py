import doctest
from typing import Union


class Bus:
    def __init__(self, number_of_bus: int, capacity: int, number_of_stops: int):
        """
        Создание и подготовка к работе объекта "Автобус".

        :param number_of_bus: Номер автобуса
        :param capacity: Вместимость
        :param number_of_stops: Количество остановок, которые проходит автобус по своему маршруту

        Примеры:
        >>> bus = Bus(145, 15, 6)               # инициализация экземпляра класса
        """
        if not isinstance(number_of_bus, int):
            raise TypeError("Номер автобуса должен быть целым числом")
        if number_of_bus <= 0:
            raise ValueError("Номер автобуса должен быть положительным числом")
        self.number_of_bus = number_of_bus

        if not isinstance(capacity, int):
            raise TypeError("Количество пассажиров должно быть целым числом")
        if capacity < 0:
            raise ValueError("Количество пассажиров должно быть положительным числом")
        self.capacity = capacity

        if not isinstance(number_of_stops, int):
            raise TypeError("Количество остановок должно быть целым числом")
        if number_of_stops <= 0:
            raise ValueError("Количество остановок должно быть положительным числом")
        self.number_of_stops = number_of_stops

    def bus_is_full(self, passengers: int) -> bool:
        """
        Метод проверки, является ли автобус полным.
        :param passengers: Количество пассажиров в автобусе на данный момент
        :return: Является ли автобус полным

        Примеры:
        >>> bus = Bus(145, 15, 6)
        >>> bus.bus_is_full(14)
        """
        if not isinstance(passengers, int):
            raise TypeError("Количество пассажиров должно быть целым числом")
        if passengers <= 0:
            raise ValueError("Количество пассажиров должно быть положительным числом")
        ...

    def control_of_payment(self, number_of_checks: int) -> bool:
        """
        Осуществлялся ли контроль на линии или нет.
        :param number_of_checks: Количество пройденных за день проверок
        :return: Пройдена ли автобусом обязательная ежедневная проверка

        Примеры:
        >>> bus = Bus(145, 15, 6)
        >>> bus.control_of_payment(0)
        """
        ...

    def need_a_petrol(self, volume: (int, float)) -> Union[int, float]:
        """
        Метод, который определяет, на сколько необходимо заполнить бак.
        :param volume: Объём бака на данный момент
        :raise ValueError: Если объём бака сейчас превышает максимальный объём
        :return: Необходимый объём бензина до полного бака

        Примеры:
        >>> bus = Bus(145, 15, 6)
        >>> bus.need_a_petrol(14.2)
        """
        ...


class Bag:
    def __init__(self, colour: str, material: str, brand: str):
        """
        Создание и подготовка к работе объекта "Сумка".
        :param colour: цвет сумки
        :param material: материал сумки
        :param brand: производитель, название магазина, бренда

        Примеры:
        >>> bag = Bag('зелёная', 'экокожа', 'Pierre Modeller')               # инициализация экземпляра класса
        """
        if not isinstance(colour, str):
            raise TypeError("Цвет сумки должен быть указан словом")
        self.colour = colour

        if not isinstance(material, str):
            raise TypeError("Материал сумки должен быть указан словом")
        self.material = material

        if not isinstance(brand, str):
            raise TypeError("Производитель должебыть типа str")
        self.brand = brand

    def size_of_bag(self, length: (int, float), width: (int, float), height: (int, float)) -> str:
        """
        Метод определяет размер сумки.
        :param length: длина сумки
        :param width: ширина сумки
        :param height: высота сумки
        :return: Размер сумки: маленькая, средняя, большая

        Примеры:
        >>> bag = Bag('зелёная', 'экокожа', 'Pierre Modeller')
        >>> bag.size_of_bag(15, 12.5, 40)
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина сумки должна быть либо int, либо float")
        if length <= 0:
            raise ValueError("Длина сумки должна быть положительным числом")

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина сумки должна быть либо int, либо float")
        if width <= 0:
            raise ValueError("Ширина сумки должна быть положительным числом")

        if not isinstance(height, (int, float)):
            raise TypeError("Высота сумки должна быть либо int, либо float")
        if height <= 0:
            raise ValueError("Высота сумки должна быть положительным числом")
        ...

    def condition(self, year_of_production: int) -> str:
        """
        Метод определяет состояние сумки.
        :param year_of_production: Год производства сумки
        :return: Состояние сумки: современная или устаревшая

        Примеры:
        >>> bag = Bag('зелёная', 'экокожа', 'Pierre Modeller')
        >>> bag.condition(2018)
        """
        if not isinstance(year_of_production, int):
            raise TypeError("Год производства должен быть типа int")
        if year_of_production <= 0:
            raise ValueError("Год производства должен быть положительным числом")
        ...


class Shop:
    def __init__(self, location: str, name: str, amount_of_cashdesks: int):
        """
        Создание и подготовка к работе объекта "Магазин".
        :param location: Месторасположение магазина, город
        :param name: Название магазина
        :param amount_of_cashdesks: Количество касс в магазине

        Примеры:
        >>> shop = Shop('Санкт-Петербург', 'Лента', 10)               # инициализация экземпляра класса
        """
        if not isinstance(location, str):
            raise TypeError("Город должен быть указан словом")
        self.location = location

        if not isinstance(name, str):
            raise TypeError("Название магазина должно быть типа str")
        self.name = name

        if not isinstance(amount_of_cashdesks, int):
            raise TypeError("Количество касс должно быть целым числом")
        if amount_of_cashdesks <= 0:
            raise ValueError("Количество касс должно быть положительным числом")
        self.amount_of_cashdesks = amount_of_cashdesks

    def diversity_of_shop(self, amount_of_products: int) -> str:
        """
        Метод проверяет разнообразие ассортимента магазина.
        :param amount_of_products: Количество представленных видов продукции.
        :return: Ассортимент: богатый, средний, бедный.

        Примеры:
        >>> shop = Shop('Санкт-Петербург', 'Лента', 10)
        >>> shop.diversity_of_shop(251)
        """
        if not isinstance(amount_of_products, int):
            raise TypeError("Количество видов продукции должно быть целым числом")
        if amount_of_products <= 0:
            raise ValueError("Количество видов продукции должно быть положительным числом")
        ...

    def hours_of_work(self, hours: (int, float)) -> Union[int, float]:
        """
        Метод определяет, сколько часов осталось работать магазину до конца рабочего дня.
        :param hours: Количество отработанных магазином за день часов
        :return: Оставшееся время работы магазина до конца рабочего дня

        Примеры:
        >>> shop = Shop('Санкт-Петербург', 'Лента', 10)
        >>> shop.hours_of_work(5.5)
        """
        if not isinstance(hours, (int, float)):
            raise TypeError("Количество отработанных часов должно быть либо типа int, либо float")
        if hours < 0:
            raise ValueError("Количество отработанных часов должно быть положительным числом")
        ...

    def number_of_departments(self, departments: int) -> int:
        """
        Метод подсчёта количество филиалов магазина.
        :param departments: Количество новых открытых (построенных) филиалов за текущий год
        :return: Новое количество филиалов магазина

        Примеры:
        >>> shop = Shop('Санкт-Петербург', 'Лента', 10)
        >>> shop.number_of_departments(3)
        """
        if not isinstance(departments, int):
            raise TypeError("Количество построенных филиалов должно быть целым числом")
        if departments < 0:
            raise ValueError("Количество построенных филиалов должно быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
