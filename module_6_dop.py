from math import pi, sqrt
class  Figure:
    sides_count = 0
    side = 1
    def __init__(self, color, sides = [side]*sides_count, filled = True):
        self.__sides = sides
        self.__color = color
        self.filled = filled
    def get_color(self):
        return list(self.__color)
    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
    def __is_valid_sides(self, *args):
        l = list(args)
        flag = True
        for i in l:
            if i < 0:
                flag = False
        if len(self.__sides) == len(l) and flag:
            return True
        else:
            return False
    def get_sides(self):
        return self.__sides
    def __len__(self):
        P = 0
        for i in self.__sides:
            P += i
        return P
    def set_sides(self, *new_sides):
        l = list(new_sides)
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    side = 1
    def __init__(self, color, radius):
        super().__init__(color)
        self.__radius = radius
    def get_square(self):
        return pi*self.__radius**2
class Triangle(Figure):
    sides_count = 3
    side = 1
    def __init__(self, color):
        super().__init__(color)
    def get_square(self):
        p = 1/2*(Figure.__sides[0] + Figure.__sides[1] + Figure.__sides[2])
        S = sqrt(p * (p - Figure.__sides[0]) * (p - Figure.__sides[1]) * (p - Figure.__sides[2]))
        return S
class Cube(Figure):
    sides_count = 12
    def __init__(self, color, side):
        super().__init__(color, sides=[side] * 12)
        self.side = side

    def get_volume(self):
        return self.side ** 3
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4)
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
