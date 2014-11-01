from core.api import pbrtPixelFilter, pbrtFilm, pbrtCamera, pbrtSurfaceIntegrator, pbrtSampler, pbrtLightSource, \
    pbrtTexture, pbrtAreaLightSource, pbrtShape, pbrtMaterial, pbrtObjectInstance, pbrtRenderer, \
    pbrtLookAt, pbrtIdentity, pbrtTranslate, pbrtAttributeBegin, pbrtAttributeEnd
from core.param_set import ParamSet
from loader.pbrt.pbrtListener import pbrtListener
from maths.point3d import Point3d
from maths.vector3d import Vector3d


class PbrtLoader(pbrtListener):
    def __init__(self):
        super(pbrtListener, self).__init__()
        self.currentParamSet = ParamSet()
        self.name = None

    # Enter a parse tree produced by pbrtParser#film.
    def enterFilm(self, ctx):
        print("enter film")
        self.currentParamSet.reset()
        self.name = str(ctx.STRING()).replace('"', '')

    # Exit a parse tree produced by pbrtParser#film.
    def exitFilm(self, ctx):
        print("exit film")
        pbrtFilm(self.name, self.currentParamSet)

    # Enter a parse tree produced by pbrtParser#pixelFilter.
    def enterPixelFilter(self, ctx):
        print("enter pixel filter")
        self.currentParamSet.reset()
        self.name = str(ctx.STRING()).replace('"', '')

    # Exit a parse tree produced by pbrtParser#pixelFilter.
    def exitPixelFilter(self, ctx):
        print("exit pixel filter")
        pbrtPixelFilter(self.name, self.currentParamSet)

    # Enter a parse tree produced by pbrtParser#paramset.
    def enterParamSet(self, ctx):

        print("enter paramset")
        p = ctx.paramSetLeft()
        a = str(p.STRING()).replace('"', '').split(' ')
        param_type = a[0]
        param_name = a[1]
        print("-->" + param_name)
        if param_type == 'point':
            print("-->point")
            i = 0
            values = []
            while True:
                if ctx.NUMBER(i) is None:
                    break
                values.append(
                    Point3d(float(str(ctx.NUMBER(i))), float(str(ctx.NUMBER(i + 1))), float(str(ctx.NUMBER(i + 2)))))
                i += 3
            self.currentParamSet.add_point(param_name, values)
        elif param_type == 'float':
            print("-->float")
            i = 0
            values = []
            while True:
                if ctx.NUMBER(i) is None:
                    break
                values.append(float(str(ctx.NUMBER(i))))
                i += 1
            self.currentParamSet.add_float(param_name, values)
        elif param_type == 'integer':
            print("-->int")
            i = 0
            values = []
            while True:
                if ctx.NUMBER(i) is None:
                    break
                values.append(int(str(ctx.NUMBER(i))))
                i += 1
            self.currentParamSet.add_int(param_name, values)
        elif param_type == 'string':
            print("-->string")
            i = 0
            values = []
            while True:
                if ctx.NUMBER(i) is None:
                    break
                values.append(int(str(ctx.STRING(i))))
                i += 1
            self.currentParamSet.add_string(param_name, values)


            # key = str(ctx.STRING(0))
            # if ctx.STRING(1) is  not None:
            # value = str(ctx.STRING(1))
            # elif ctx.INT() is not None:
            # value = ctx.INT()
            #       elif ctx.FLOAT() is not None:
            #           value = ctx.FLOAT()
            #       print("->("+ str(key)+","+str(value)+")")

    # Exit a parse tree produced by pbrtParser#paramset.
    def exitParamSet(self, ctx):
        print("exit paramset")

    # Enter a parse tree produced by pbrtParser#lookAt.
    def enterLookAt(self, ctx):
        print("enter look at")
        e = Vector3d(float(str(ctx.vector3(0).NUMBER(0))), float(str(ctx.vector3(0).NUMBER(1))), float(str(ctx.vector3(0).NUMBER(2))))
        l = Vector3d(float(str(ctx.vector3(1).NUMBER(0))), float(str(ctx.vector3(1).NUMBER(1))), float(str(ctx.vector3(1).NUMBER(2))))
        u = Vector3d(float(str(ctx.vector3(2).NUMBER(0))), float(str(ctx.vector3(2).NUMBER(1))), float(str(ctx.vector3(2).NUMBER(2))))
        pbrtLookAt(e, l, u)

    # Exit a parse tree produced by pbrtParser#lookAt.
    def exitLookAt(self, ctx):
        print("exit look at")

    # Enter a parse tree produced by pbrtParser#program.
    def enterProgram(self, ctx):
        pass

    # Exit a parse tree produced by pbrtParser#program.
    def exitProgram(self, ctx):
        pass

    # Enter a parse tree produced by pbrtParser#camera.
    def enterCamera(self, ctx):
        print("enter camera")
        self.currentParamSet.reset()
        self.name = str(ctx.STRING()).replace('"', '')

    # Exit a parse tree produced by pbrtParser#camera.
    def exitCamera(self, ctx):
        print("exit camera")
        pbrtCamera(self.name, self.currentParamSet)

    # Enter a parse tree produced by pbrtParser#surfaceIntegrator.
    def enterSurfaceIntegrator(self, ctx):
        print("enter surface surface_integrator")
        self.currentParamSet.reset()
        self.name = str(ctx.STRING()).replace('"', '')

    # Exit a parse tree produced by pbrtParser#surfaceIntegrator.
    def exitSurfaceIntegrator(self, ctx):
        print("exit surface surface_integrator")
        pbrtSurfaceIntegrator(self.name, self.currentParamSet)

    # Enter a parse tree produced by pbrtParser#vector3.
    def enterVector3(self, ctx):
        print("enter vector3")

    # Exit a parse tree produced by pbrtParser#vector3.
    def exitVector3(self, ctx):
        print("exit vector3")

    # Enter a parse tree produced by pbrtParser#sampler.
    def enterSampler(self, ctx):
        print("enter sampler")
        self.currentParamSet.reset()
        self.name = str(ctx.STRING()).replace('"', '')

    # Exit a parse tree produced by pbrtParser#sampler.
    def exitSampler(self, ctx):
        print("exit sampler")
        pbrtSampler(self.name, self.currentParamSet)

        # Enter a parse tree produced by pbrtParser#body.

    def enterBody(self, ctx):
        pass

    # Exit a parse tree produced by pbrtParser#body.
    def exitBody(self, ctx):
        pass

    # Enter a parse tree produced by pbrtParser#scale.
    def enterScale(self, ctx):
        print("enter scale")
        pass

    # Exit a parse tree produced by pbrtParser#scale.
    def exitScale(self, ctx):
        print("exit scale")
        pass

    # Enter a parse tree produced by pbrtParser#rotate.
    def enterRotate(self, ctx):
        print("enter rotate")
        pass

    # Exit a parse tree produced by pbrtParser#rotate.
    def exitRotate(self, ctx):
        print("exit rotate")
        pass

    # Enter a parse tree produced by pbrtParser#transform.
    def enterTransform(self, ctx):
        print("enter transform")
        pass

    # Exit a parse tree produced by pbrtParser#transform.
    def exitTransform(self, ctx):
        print("exit transform")
        pass

    # Enter a parse tree produced by pbrtParser#lightSource.
    def enterLightSource(self, ctx):
        print("enter lightsource lock")
        self.currentParamSet.reset()
        self.name = str(ctx.STRING()).replace('"', '')

    # Exit a parse tree produced by pbrtParser#lightSource.
    def exitLightSource(self, ctx):
        print("exit lightsource lock")
        pbrtLightSource(self.name, self.currentParamSet)

    # Enter a parse tree produced by pbrtParser#transformBlock.
    def enterTransformBlock(self, ctx):
        print("enter trnasform block")
        pass

    # Exit a parse tree produced by pbrtParser#transformBlock.
    def exitTransformBlock(self, ctx):
        print("exit trnasform block")
        pass

    # Enter a parse tree produced by pbrtParser#texture.
    def enterTexture(self, ctx):
        print("enter texture block")
        self.currentParamSet.reset()
        self.name = str(ctx.STRING()).replace('"', '')

    # Exit a parse tree produced by pbrtParser#texture.
    def exitTexture(self, ctx):
        print("exit texture block")
        pbrtTexture(self.name, self.currentParamSet)

    # Enter a parse tree produced by pbrtParser#areaLightSource.
    def enterAreaLightSource(self, ctx):
        self.currentParamSet.reset()
        self.name = str(ctx.STRING()).replace('"', '')

    # Exit a parse tree produced by pbrtParser#areaLightSource.
    def exitAreaLightSource(self, ctx):
        pbrtAreaLightSource(self.name, self.currentParamSet)

    # Enter a parse tree produced by pbrtParser#shape.
    def enterShape(self, ctx):
        print("enter shape block")
        self.currentParamSet.reset()
        self.name = str(ctx.STRING()).replace('"', '')

    # Exit a parse tree produced by pbrtParser#shape.
    def exitShape(self, ctx):
        print("exit shape block")
        pbrtShape(self.name, self.currentParamSet)

    # Enter a parse tree produced by pbrtParser#material.
    def enterMaterial(self, ctx):
        print("enter material block")
        self.currentParamSet.reset()
        self.name = str(ctx.STRING()).replace('"', '')

    # Exit a parse tree produced by pbrtParser#material.
    def exitMaterial(self, ctx):
        print("exit material  block")
        pbrtMaterial(self.name, self.currentParamSet)

    # Enter a parse tree produced by pbrtParser#renderer.
    def enterRenderer(self, ctx):
        print("enter renderer block")
        self.currentParamSet.reset()
        self.name = str(ctx.STRING()).replace('"', '')
        pass

    # Exit a parse tree produced by pbrtParser#renderer.
    def exitRenderer(self, ctx):
        print("exit material  block")
        pbrtRenderer(self.name, self.currentParamSet)

    # Enter a parse tree produced by pbrtParser#include.
    def enterInclude(self, ctx):
        pass

    # Exit a parse tree produced by pbrtParser#include.
    def exitInclude(self, ctx):
        pass

    # Enter a parse tree produced by pbrtParser#worldBlock.
    def enterWorldBlock(self, ctx):
        print("enter world block")
        pbrtIdentity()

    # Exit a parse tree produced by pbrtParser#worldBlock.
    def exitWorldBlock(self, ctx):
        print("exit world block")
        pass

    # Enter a parse tree produced by pbrtParser#objectInstance.
    def enterObjectInstance(self, ctx):
        print("enter object block")
        self.currentParamSet.reset()
        self.name = str(ctx.STRING()).replace('"', '')

    # Exit a parse tree produced by pbrtParser#objectInstance.
    def exitObjectInstance(self, ctx):
        print("exit object block")
        pbrtObjectInstance(self.name)

    # Enter a parse tree produced by pbrtParser#translate.
    def enterTranslate(self, ctx):
        print("enter translate block")
        a = float(str(ctx.NUMBER(0)))
        b = float(str(ctx.NUMBER(1)))
        c = float(str(ctx.NUMBER(2)))
        pbrtTranslate(a, b, c)

    # Exit a parse tree produced by pbrtParser#translate.
    def exitTranslate(self, ctx):
        print("exit translate block")
        pass

    # Enter a parse tree produced by pbrtParser#objectBlock.
    def enterObjectBlock(self, ctx):
        print("enter object block")
        pass

    # Exit a parse tree produced by pbrtParser#objectBlock.
    def exitObjectBlock(self, ctx):
        print("exit object block")
        pass

    # Enter a parse tree produced by pbrtParser#attributeBlock.
    def enterAttributeBlock(self, ctx):
        print("enter attribute block")
        pbrtAttributeBegin()

    # Exit a parse tree produced by pbrtParser#attributeBlock.
    def exitAttributeBlock(self, ctx):
        print("exit attribute block")
        pbrtAttributeEnd()
