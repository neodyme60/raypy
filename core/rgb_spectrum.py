from core.coefficient_spectrum import CoefficientSpectrum

CONST_RGB_SAMPLES = 3

class RGBSpectrum(CoefficientSpectrum):

    def __init__(self, value: float=0.0):
        super().__init__(value, CONST_RGB_SAMPLES)

    @staticmethod
    def create_from_coefficient_spectrum(cs: CoefficientSpectrum):
        ret = RGBSpectrum()