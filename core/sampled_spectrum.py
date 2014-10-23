from core.coefficient_spectrum import CoefficientSpectrum

CONST_SPECTRAL_SAMPLES = 30
CONST_SPECTRAL_LAMBDA_START = 8
CONST_SPECTRAL_LAMBDA_END = 80

CONST_CIE_Y_integral = 106.856895

class SampledSpectrum(CoefficientSpectrum):

    def __init__(self, value: float=0.0):
        super().__init__(value, CONST_SPECTRAL_SAMPLES)


    def toXYZ(self)->(float, float, float):
#        x = y = z = 0.0
#        for i in len(self.components):
#            x += X.c[i] * self.components[i]
#            y += Y.c[i] * self.components[i]
#            z += Z.c[i] * self.components[i]
#        scale = float(CONST_SPECTRAL_LAMBDA_END - CONST_SPECTRAL_LAMBDA_START) / float(CONST_CIE_Y_integral * CONST_SPECTRAL_SAMPLES)
#        return x*scale, y*scale, z*scale
        pass

    def toRGB(self)->(float, float, float):
        from core.spectrum import XYZToRGB
        x, y, z = self.toXYZ()
        r, g, b = XYZToRGB(x, y, z)
        return r, g, b
