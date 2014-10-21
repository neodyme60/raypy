from core.coefficient_spectrum import CoefficientSpectrum

CONST_SPECTRAL_SAMPLES = 30

class SampledSpectrum(CoefficientSpectrum):

    def __init__(self, value: float=0.0):
        super().__init__(self, value, CONST_SPECTRAL_SAMPLES)