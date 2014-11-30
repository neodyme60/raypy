import math
from core.spectrum import Spectrum
from maths.tools import get_clamp


def FrDiel(cosi: float, cost: float, etai: Spectrum, etat: Spectrum)->Spectrum:
    Rparl = ((etat * cosi) - (etai * cost)) / ((etat * cosi) + (etai * cost))
    Rperp = ((etai * cosi) - (etat * cost)) / ((etai * cosi) + (etat * cost))
    return (Rparl*Rparl + Rperp*Rperp) / 2.0


def FrCond(cosi: float, eta: Spectrum, k: Spectrum)->Spectrum:
    tmp = (eta*eta + k*k) * cosi*cosi
    Rparl2 = (tmp - (2.0 * eta * cosi) + 1) / (tmp + (2.0 * eta * cosi) + 1)
    tmp_f = eta*eta + k*k
    Rperp2 = (tmp_f - (2.0 * eta * cosi) + cosi*cosi) / (tmp_f + (2.0 * eta * cosi) + cosi*cosi)
    return (Rparl2 + Rperp2) / 2.0

class Fresnel():
    def __init__(self):
        pass

    #Fresnel Interface
    def Evaluate(self, cosi: float)->Spectrum:
        raise NotImplemented

class FresnelConductor(Fresnel):
    def __init__(self,  e: Spectrum, kk: Spectrum):
        super().__init__()
        self.eta = e
        self.k = kk

    # FresnelConductor Public Methods
    def Evaluate(self, cosi: float)->Spectrum:
        return FrCond(math.fabs(cosi), self.eta, self.k)


class FresnelDielectric(Fresnel):
    def __init__(self, ei:float , et: float):
        super().__init__()
        self.eta_i = ei
        self.eta_t = et

    def Evaluate(self, cosi: float)->Spectrum:
        cosi = get_clamp(cosi, -1.0, 1.0)

        # Compute indices of refraction for dielectric
        entering = cosi > 0.0
        ei = self.eta_i, et = self.eta_t
        if entering:
            ei, et = et, ei

        # Compute _sint_ using Snell's law
        sint = ei/et * math.sqrt(max(0.0, 1.0 - cosi*cosi))
        if sint >= 1.0:
            # Handle total internal reflection
            return 1.0
        else:
            cost = math.sqrt(max(0.0, 1.0 - sint*sint))
            return FrDiel(math.fabs(cosi), cost, ei, et)


class FresnelNoOp(Fresnel):
    def __init__(self):
        super().__init__()

    def Evaluate(self, cosi: float)->Spectrum:
        return Spectrum(1.0)
