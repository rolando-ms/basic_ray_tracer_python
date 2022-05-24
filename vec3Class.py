import numpy as np

class vec3:
    def __init__(self, vector: np.array = np.zeros(3)):
        self.e = vector
        self.x = self.e[0]
        self.y = self.e[1]
        self.z = self.e[2]

    def __str__(self):
        return 'e[0] = {0}, e[1] = {1}, e[2] = {2}'.format(self.e[0], self.e[1], self.e[2])

    def length(self):
        return np.sqrt(self.length_squared())

    def length_squared(self):
        return np.sum(self.e * self.e)

    def unit_vector(self):
        return self.e / self.length()

