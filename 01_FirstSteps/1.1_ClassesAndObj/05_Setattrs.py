"""
Подвиг 5. Объявите пустой класс с именем Car.
С помощью функции setattr() добавьте в этот класс атрибуты:
model: "Тойота"
color: "Розовый"
number: "П111УУ77"
Выведите на экран значение атрибута color, используя словарь __dict__ класса Car.
"""


class Car:
    pass


# Car.model = "Тойота"
# Car.color = "Розовый"
# Car.number = "П111УУ77"

setattr(Car, "model", "Тойота")
setattr(Car, "color", "Розовый")
setattr(Car, "number", "П111УУ77")

print(Car.__dict__["color"])


