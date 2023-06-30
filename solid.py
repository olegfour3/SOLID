# Пример: Расчет площади разных геометрических фигур

from abc import ABC, abstractmethod
from math import pi


# Принцип единственной ответственности (Single Responsibility Principle)
# Классы должны иметь только одну причину для изменения.

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2


# Принцип открытости/закрытости (Open/Closed Principle)
# Программные сущности должны быть открыты для расширения, но закрыты для изменения.

class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()
        return total


# Принцип подстановки Барбары Лисков (Liskov Substitution Principle)
# Объекты в программе должны быть заменяемыми на экземпляры их подтипов без изменения корректности программы.

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


# Принцип разделения интерфейса (Interface Segregation Principle)
# Клиенты не должны зависеть от интерфейсов, которые они не используют.

class VolumeCalculator(Shape):
    def __init__(self, shapes):
        self.shapes = shapes

    def calculate_volume(self):
        total = 0
        for shape in self.shapes:
            if isinstance(shape, ThreeDimensionalShape):
                total += shape.calculate_volume()
        return total


# Принцип инверсии зависимостей (Dependency Inversion Principle)
# Зависимости должны строиться относительно абстракций, а не от конкретных реализаций.

class ThreeDimensionalShape(ABC):
    @abstractmethod
    def calculate_volume(self):
        pass


class Sphere(ThreeDimensionalShape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_volume(self):
        return (4 / 3) * pi * self.radius ** 3


# Использование кода

shapes = [Rectangle(5, 10), Circle(7), Square(3), Sphere(2)]
area_calculator = AreaCalculator(shapes)
volume_calculator = VolumeCalculator(shapes)

total_area = area_calculator.total_area()
total_volume = volume_calculator.calculate_volume()

print(f"Total area: {total_area}")
print(f"Total volume: {total_volume}")
