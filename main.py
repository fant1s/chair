class chair:
    def __init__(self, legs, size, material):
        self.material = material
        self.legs = legs
        self.size = size

    def __str__(self):
        return f'Стул(Материал: {my_chair.material}, Кол-во ножек: {my_chair.legs}, Размер сидалища: {my_chair.size})'

    def __eq__(self, other):
        if isinstance(other, chair):
            return self.legs == other.legs
        return False

    def __ne__(self, other):
        if isinstance(other, chair):
            return self.legs != other.legs
        return False

    def __lt__(self, other):
        if isinstance(other, chair):
            return self.legs < other.legs
        return False

    def __le__(self, other):
        if isinstance(other, chair):
            return self.legs <= other.legs
        return False

    def __gt__(self, other):
        if isinstance(other, chair):
            return self.legs > other.legs
        return False

    def __ge__(self, other):
        if isinstance(other, chair):
            return self.legs >= other.legs
        return False

    def __repr__(self):
        return f'Стул(Материал: {my_chair.material}, Кол-во ножек: {my_chair.legs}, Размер сидалища: {my_chair.size})'

my_chair = chair(3, 52, 'Дуб')
my_chair2 = chair(3, 52, 'Дуб')
c = sorted([my_chair2, my_chair])
print(c)

print(my_chair > my_chair2)



