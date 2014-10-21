from copy import copy
import math

from maths.config import infinity_max_f
from maths.tools import get_clamp


class CoefficientSpectrum:
    def __init__(self, samples_count: int, values: float=0.0):
        self.components = [values] * samples_count

    @staticmethod
    def create_from_coefficient_spectrum(cs: CoefficientSpectrum):
        ret = copy(cs)
        return ret

    def __add__(self, other):
        ret = copy(self)
        if type(other) == CoefficientSpectrum:
            for i in range(len(self.components)):
                ret.components[i] += other.components[i]
        elif type(other) == float:
            for i in range(len(self.components)):
                ret.components[i] += other
        return ret

    def __iadd__(self, other):
        if type(other) == CoefficientSpectrum:
            for i in range(len(self.components)):
                self.components[i] += other.components[i]
        elif type(other) == float:
            for i in range(len(self.components)):
                self.components[i] += other
        return self

    def __sub__(self, other):
        ret = copy(self)
        if type(other) == CoefficientSpectrum:
            for i in range(len(self.components)):
                ret.components[i] -= other.components[i]
        elif type(other) == float:
            for i in range(len(self.components)):
                ret.components[i] -= other
        return ret

    def __isub__(self, other):
        if type(other) == CoefficientSpectrum:
            for i in range(len(self.components)):
                self.components[i] -= other.components[i]
        elif type(other) == float:
            for i in range(len(self.components)):
                self.components[i] -= other
        return self

    def __idiv__(self, other):
        ret = copy(self)
        if type(other) == CoefficientSpectrum:
            for i in range(len(self.components)):
                ret.components[i] /= other.components[i]
        elif type(other) == float:
            for i in range(len(self.components)):
                self.components[i] /= other
        return ret

    def __div__(self, other):
        if type(other) == CoefficientSpectrum:
            for i in range(len(self.components)):
                self.components[i] /= other.components[i]
        elif type(other) == float:
            for i in range(len(self.components)):
                self.components[i] /= other
        return self

    def __imul__(self, other):
        ret = copy(self)
        if type(other) == CoefficientSpectrum:
            for i in range(len(self.components)):
                ret.components[i] *= other.components[i]
        elif type(other) == float:
            for i in range(len(self.components)):
                ret.components[i] *= other
        return ret

    def __mul__(self, other):
        if type(other) == CoefficientSpectrum:
            for i in range(len(self.components)):
                self.components[i] *= other.components[i]
        elif type(other) == float:
            for i in range(len(self.components)):
                self.components[i] *= other
        return self

    def __eq__(self, other):
        assert type(other) == CoefficientSpectrum
        for i in range(len(self.components)):
            if self.components[i] != other.components[i]:
                return False
        return True

    def __ne__(self, other):
        return not __eq__(self, other)

    def __neg__(self):
        for i in range(len(self.components)):
            self.components[i] = -self.components[i]
        return self

    def get_is_zero(self):
        for i in range(len(self.components)):
            if self.components[i] != 0.0:
                return False
        return True

    def get_sqrt(self):
        ret = copy(self)
        for i in range(len(self.components)):
            ret.components[i] = math.sqrt(ret.components[i])

    def get_exp(self):
        ret = copy(self)
        for i in range(len(self.components)):
            ret.components[i] = math.exp(ret.components[i])

    def get_clamp(self, low: float=0.0, high: float=infinity_max_f):
        ret = copy(self)
        for i in range(len(self.components)):
            ret.components[i] = get_clamp(ret.components[i], low, high)

    def get_has_nan(self):
        for i in range(len(self.components)):
            if math.isnan(self.components[i]):
                return True
        return False
