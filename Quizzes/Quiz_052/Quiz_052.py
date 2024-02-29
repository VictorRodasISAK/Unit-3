class Bicycle:
    def __init__(self, material: str, size: int):
        self.material = material
        self.wheels = Wheel(size)

    def ride(self):
        return self.material


class Wheel:
    def __init__(self, size: int):
        self.size = size

    def get_size(self):
        return self.size

    def get_perimeter(self):
        return self.get_size() * 2.54 * 3.14

    def get_rotation_per_km(self):
        return round(100000 / self.get_perimeter(), 2)


test = Bicycle("Aluminium", 26)
print(test.ride())

test2 = Wheel(26)
print(test2.get_rotation_per_km())
