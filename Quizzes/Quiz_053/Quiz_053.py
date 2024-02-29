class PalNum():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_pal_list(self):
        pal_list = []
        for i in range(self.a, self.b + 1):
            a = ""
            for x in str(i):
                a = x + a
            if str(i) == a:
                pal_list.append(i)
        return pal_list

test = PalNum(1, 9)
test2 = PalNum(10, 199)
print(test.get_pal_list())
print(test2.get_pal_list())


