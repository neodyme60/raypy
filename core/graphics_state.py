import core.api
from core.param_set import ParamSet
from core.texture_param_set import TextureParamSet


class GraphicsState():

    def __init__(self):
        self.floatTextures = {}
        self.spectrumTextures = {}
        self.material = "matte"
        self.materialParams = ParamSet()
        self.currentNamedMaterial = ""
        self.namedMaterials = {}
        self.areaLight = ""
        self.areaLightParams = None

    def CreateMaterial(self, params: ParamSet):
        global graphicsState

        mtl = None

        mp = TextureParamSet(params, self.materialParams, self.floatTextures, self.spectrumTextures)
        if self.currentNamedMaterial!="" and (self.currentNamedMaterial in self.namedMaterials):
            mtl = self.namedMaterials[graphicsState.currentNamedMaterial]
        if mtl is None:
            mtl = core.api.make_material(self.material, core.api.curTransform[0], mp)
        if mtl is None:
            mtl = core.api.make_material("matte", core.api.curTransform[0], mp)
        if mtl is None:
            raise Exception("Unable to create \"matte\" material?!")
        return mtl