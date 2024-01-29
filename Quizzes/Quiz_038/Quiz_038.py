import matplotlib.pyplot as plt
import random
class Saleman_Map:
    def __init__(self):
        self.x = []
        self.y = []
        self.name = []

    def generate_data(self, name):
        self.name = name
        for i in range(len(name)):
            self.x.append(random.randint(0, 100))
            self.y.append(random.randint(0, 100))

    def generate_map(self):
        plt.scatter(self.x, self.y)
        for i, city in enumerate(self.name):
            plt.text(self.x[i], self.y[i], city, fontsize=8)

        plt.title('Nagano Map')
        plt.xlabel('Distance (Km)')
        plt.ylabel('Distance (Km)')
        plt.show()

# Example usage:
salesman_map = Saleman_Map()
salesman_map.generate_data(['Sapporo', 'Fukuoka', 'Nagoya', 'Osaka', 'Kobe', 'Kawasaki', 'Kyoto', 'Saitama', 'Yokohama'])
salesman_map.generate_map()







