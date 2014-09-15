class Sampler:

    def __init__(self, xstart:int, xend:int, ystart:int, yend:int, spp:int, sopen:float, sclose:float):
        self.xPixelStart = xstart
        self.xPixelEnd = xend
        self.yPixelStart = ystart
        self.yPixelEnd = yend
        self.samplesPerPixel = spp
        self.shutterOpen = sopen
        self.shutterClose = sclose

