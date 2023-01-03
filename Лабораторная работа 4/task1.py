import doctest

if __name__ == "__main__":
    class Shop:
        """Базовый класс магазина."""
        shop_count = 0          # атрибут класса

        def __init__(self, name: str, location: str, departments: int):
            """
            Создание и подготовка к работе объекта "Магазин".
            :param name: Название магазина
            :param location: Месторасположение магазина, город
            :param departments: Количество филиалов магазина

            Примеры:
            >>> shop = Shop('Лента', 'Санкт-Петербург', 100)               # инициализация экземпляра класса
            """

            self._name = name                           # защищённый атрибут
            self._location = location                   # защищённый атрибут
            self._departments = departments             # защищённый атрибут
            self.increment_shop_count()

        @classmethod
        def increment_shop_count(cls) -> int:
            """Метод, который увеличивает количество магазинов."""
            cls.shop_count += 1

        @property
        def name(self) -> str:
            return self._name

        @name.setter
        def name(self, new_name: str) -> None:
            if not isinstance(new_name, str):
                raise TypeError
            self._name = new_name

        @property
        def location(self):
            return self._location

        @location.setter
        def location(self, new_location: str) -> None:
            if not isinstance(new_location, str):
                raise TypeError
            self._location = new_location

        @property
        def departments(self):
            return self._departments

        @departments.setter
        def departments(self, new_departments: int) -> None:
            if not isinstance(new_departments, int):
                raise TypeError
            self._departments = new_departments

        def __str__(self):
            return f"Магазин {self._name}, расположенный в {self._location}."

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self._name!r}, location={self._location!r}, departments={self._departments!r})"

        def number_of_departments(self, built_departments: int) -> int:
            """
            Метод подсчёта количества филиалов магазина.
            :param built_departments: Количество построенных филиалов за текущий год
            :return: Новое количество филиалов магазина

            Примеры:
            >>> shop = Shop('Лента', 'Санкт-Петербург', 100)
            >>> shop.number_of_departments(3)
            """
            if not isinstance(built_departments, int):
                raise TypeError("Количество построенных филиалов должно быть целым числом")
            if built_departments < 0:
                raise ValueError("Количество построенных филиалов должно быть положительным числом")
            answer = self._departments + built_departments
            print(answer)

    class Prodcuts(Shop):
        """Дочерний класс - продуктовый магазин."""
        def __init__(self, name: str, location: str, departments: int, stock: int):
            super().__init__(name, location, departments)
            super().__str__()
            super().increment_shop_count()
            self.stock = None              # ассортимент продуктов
            self.set_stock(stock)

        def set_stock(self, new_stock: int):
            """Инкапсуляция использована для проверки на коректность присваиваемого поля."""
            if not isinstance(new_stock, int):
                raise TypeError("Количество продуктов должно быть целым числом")
            if new_stock < 0:
                raise ValueError("Количество продуктов должно быть положительным числом")
            self.stock = new_stock

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self._name!r}, location={self._location!r}, departments={self._departments!r}, stock={self.stock!r})"

        def number_of_departments(self, built_departments: int) -> int:
            """
            Осуществляется перегрузка данного метода для уточнения количества филиалов конкретного продуктового магазина.
            :param built_departments: Количество построенных филиалов за текущий год
            :return: Новое количество филиалов магазина
            """
            answer = self._departments + built_departments
            print(f"Магазин {self.name}, входящий в группу {self.__class__.__name__}, имеет {answer} филиалов.")

    doctest.testmod()
    pass
