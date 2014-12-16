from core.rgb_spectrum import RGBSpectrum


def XYZToRGB(x: float, y: float, z: float)->(float, float, float):
    return 3.240479*x - 1.537150*y - 0.498535*z, -0.969256*x + 1.875991*y + 0.041556*z, 0.055648*x - 0.204043*y + 1.057311*z

def RGBToXYZ(r: float, g: float, b: float)->(float, float, float):
    return 0.412453*r + 0.357580*g + 0.180423*b, 0.212671*r + 0.715160*g + 0.072169*g,0.019334*r + 0.119193*g + 0.950227*b

def y(self)->float:
        raise NotImplemented

Spectrum = RGBSpectrum
#else:
#    Spectrum = SampledSpectrum

