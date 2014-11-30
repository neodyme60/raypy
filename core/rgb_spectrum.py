from core.coefficient_spectrum import CoefficientSpectrum

CONST_RGB_SAMPLES = 3

class RGBSpectrum(CoefficientSpectrum):

    def __init__(self, value: float=0.0):
        super().__init__(value, CONST_RGB_SAMPLES)

    def toXYZ(self)->(float, float, float):
        from core.spectrum import RGBToXYZ
        x, y, z = RGBToXYZ(self.components[0], self.components[1], self.components[2])
        return x, y, z

    def toRGB(self)->(float, float, float):
        return self.components[0], self.components[1], self.components[2]
