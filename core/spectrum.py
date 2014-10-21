class Spectrum:

    def __init__(self):
        self.components = list()

    def __mul__(self, other):
        s = Spectrum()
        if type(other)==float:
            for i in self.components:
                s.components.append(i * other)
        elif type(other)==Spectrum:
            assert len(other.compoents)==len(self.components)
            for i in range(0, len(self.components)):
                s.components.append(self.components[i] * other.compoents[i])
        return s
