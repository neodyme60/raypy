
# Monte Carlo Utility Declarations
from copy import deepcopy


class Distribution1D():

    def __init__(self, f: [float]):
        self.func = list(f)
        self.cdf = [float] * (len(self.func)+1)
        self.count = len(self.func)

        # Compute integral of step function at $x_i$
        self.cdf[0] = 0.0
        for i in range(1, self.count+1):
            self.cdf[i] = self.cdf[i-1] + self.func[i-1] / self.count

        # Transform step function integral into CDF
        self.funcInt = self.cdf[self.count]
        if self.funcInt == 0.0:
            for i in range(self.count+1):
                self.cdf[i] = float(i) / float(self.count)
        else:
            for i in range(self.count+1):
                self.cdf[i] /= float(self.funcInt)

    def SampleContinuous(self, u: float, pdf: [float]=None, off: [int]=None)->float:
        pass
        # Find surrounding CDF segments and _offset_
#        float *ptr = std::upper_bound(self.cdf, self.cdf+self.count+1, u)
#        offset = max(0, int(ptr-self.cdf-1))
#        if off is not None:
#            off = offset
#        Assert(offset < count)
#        Assert(u >= cdf[offset] && u < cdf[offset+1])

        # Compute offset along CDF segment
#        du = (u - self.cdf[offset]) / (self.cdf[offset+1] - self.cdf[offset])
#        Assert(!isnan(du))

        # Compute PDF for sampled offset
#        if pdf:
#            pdf = self.func[offset] / funcInt

        # Return $x\in{}[0,1)$ corresponding to sample
#        return (offset + du) / self.count

    def SampleDiscrete(self, u: float)->(float, int):
        offset = 0
        for i in range(1, len(self.cdf)):
            if self.cdf[i] > u:
                offset = i-1
                break
        pdf = self.func[offset] / (self.funcInt * self.count)
        return pdf, offset

