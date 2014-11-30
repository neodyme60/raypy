from copy import copy, deepcopy
import math

from maths.config import infinity_max_f
import maths.tools


class CoefficientSpectrum:

    def __init__(self, values: float, samples_count: int):
        self.components = [values] * samples_count

    @staticmethod
    def create_from_array(components: [float]):
        coef = CoefficientSpectrum(0.0, len(components))
        for i in range(len(components)):
           coef.components[i] = components[i]
        return coef

    def __add__(self, other):
        ret = deepcopy(self)
        if isinstance(other, CoefficientSpectrum):
            for i in range(len(self.components)):
                ret.components[i] += other.components[i]
        elif isinstance(other, float):
            for i in range(len(self.components)):
                ret.components[i] += other
        return ret

    def __iadd__(self, other):
        if isinstance(other, CoefficientSpectrum):
            for i in range(len(self.components)):
                self.components[i] += other.components[i]
        elif isinstance(other, float):
            for i in range(len(self.components)):
                self.components[i] += other
        return self

    def __sub__(self, other):
        ret = deepcopy(self)
        if isinstance(other, CoefficientSpectrum):
            for i in range(len(self.components)):
                ret.components[i] -= other.components[i]
        elif isinstance(other, float):
            for i in range(len(self.components)):
                ret.components[i] -= other
        return ret

    def __isub__(self, other):
        if isinstance(other, CoefficientSpectrum):
            for i in range(len(self.components)):
                self.components[i] -= other.components[i]
        elif isinstance(other, float):
            for i in range(len(self.components)):
                self.components[i] -= other
        return self

    def __idiv__(self, other):
        if isinstance(other, CoefficientSpectrum):
            for i in range(len(self.components)):
                self.components[i] /= other.components[i]
        elif isinstance(other, float):
            for i in range(len(self.components)):
                self.components[i] /= other
        return self

    def __div__(self, other):
        ret = deepcopy(self)
        if isinstance(other, CoefficientSpectrum):
            for i in range(len(self.components)):
                ret.components[i] /= other.components[i]
        elif isinstance(other, float):
            for i in range(len(self.components)):
                ret.components[i] /= other
        return ret

    def __truediv__(self, other):
        ret = deepcopy(self)
        if isinstance(other, CoefficientSpectrum):
            for i in range(len(self.components)):
                ret.components[i] /= other.components[i]
        elif isinstance(other, float):
            for i in range(len(self.components)):
                ret.components[i] /= other
        return ret

    def __imul__(self, other):
        if isinstance(other, CoefficientSpectrum):
            for i in range(len(self.components)):
                self.components[i] *= other.components[i]
        elif isinstance(other, float):
            for i in range(len(self.components)):
                self.components[i] *= other
        return self

    def __mul__(self, other):
        ret = deepcopy(self)
        if isinstance(other, CoefficientSpectrum):
            for i in range(len(self.components)):
                ret.components[i] *= other.components[i]
        elif isinstance(other, float):
            for i in range(len(self.components)):
                ret.components[i] *= other
        return ret

    def __eq__(self, other):
        assert isinstance(other, CoefficientSpectrum)
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

    def get_is_black(self):
        return self.get_is_zero()

    def get_sqrt(self):
        ret = deepcopy(self)
        for i in range(len(self.components)):
            ret.components[i] = math.sqrt(ret.components[i])
        return ret

    def get_exp(self):
        ret = deepcopy(self)
        for i in range(len(self.components)):
            ret.components[i] = math.exp(ret.components[i])
        return ret

    def get_clamp(self, low: float=0.0, high: float=infinity_max_f):
        ret = deepcopy(self)
        for i in range(len(self.components)):
            ret.components[i] = maths.tools.get_clamp(ret.components[i], low, high)
        return  ret

    def get_has_nan(self):
        for i in range(len(self.components)):
            if math.isnan(self.components[i]):
                return True
        return False

    def set(self, value: float):
        for i in range(len(self.components)):
            self.components[i]=value
        return self