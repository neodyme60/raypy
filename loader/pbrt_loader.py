from loader.pbrt.pbrtListener import pbrtListener


class PbrtLoader(pbrtListener):

    def __init__(self):
        super(pbrtListener, self).__init__()

    # Enter a parse tree produced by pbrtParser#film.
    def enterFilm(self, ctx):
        print("enter film")
        print("->type:" + str(ctx.STRING()))

    # Exit a parse tree produced by pbrtParser#film.
    def exitFilm(self, ctx):
        print("exit film")

    # Enter a parse tree produced by pbrtParser#pixelFilter.
    def enterPixelFilter(self, ctx):
        print("enter pixel filter")
        print("->type:" + str(ctx.STRING()))

    # Exit a parse tree produced by pbrtParser#pixelFilter.
    def exitPixelFilter(self, ctx):
        print("exit pixel filter")

    # Enter a parse tree produced by pbrtParser#paramsetitem.
    def enterParamsetitem(self, ctx):
        print("enter paramsetitem")
        pass

    # Exit a parse tree produced by pbrtParser#paramsetitem.
    def exitParamsetitem(self, ctx):
        print("exit paramsetitem")
        pass

    # Enter a parse tree produced by pbrtParser#paramset.
    def enterParamset(self, ctx):
        print("enter paramset")
 #       key = str(ctx.STRING(0))
 #       if ctx.STRING(1) is  not None:
 #          value = str(ctx.STRING(1))
 #       elif ctx.INT() is not None:
 #           value = ctx.INT()
 #       elif ctx.FLOAT() is not None:
 #           value = ctx.FLOAT()
 #       print("->("+ str(key)+","+str(value)+")")

    # Exit a parse tree produced by pbrtParser#paramset.
    def exitParamset(self, ctx):
        print("exit paramset")
        pass

    # Enter a parse tree produced by pbrtParser#lookAt.
    def enterLookAt(self, ctx):
        print("enter look at")
        v1 = ctx.vector3(0)
        v2 = ctx.vector3(1)
        v3 = ctx.vector3(2)
        print("->v1: (" +
              str(v1.FLOAT(0)) + "," +
              str(v1.FLOAT(1)) + "," +
              str(v1.FLOAT(2)) + ")"
              )
        print("->v2: (" +
              str(v2.FLOAT(0)) + "," +
              str(v2.FLOAT(1)) + "," +
              str(v2.FLOAT(2)) + ")"
              )

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
        print("->type:" + str(ctx.STRING()))

    # Exit a parse tree produced by pbrtParser#camera.
    def exitCamera(self, ctx):
        print("exit camera")

    # Enter a parse tree produced by pbrtParser#surfaceIntegrator.
    def enterSurfaceIntegrator(self, ctx):
        print("enter surface surface_integrator")
        print("->type:" + str(ctx.STRING()))

    # Exit a parse tree produced by pbrtParser#surfaceIntegrator.
    def exitSurfaceIntegrator(self, ctx):
        print("exit surface surface_integrator")

    # Enter a parse tree produced by pbrtParser#vector3.
    def enterVector3(self, ctx):
        print("enter vector3")

    # Exit a parse tree produced by pbrtParser#vector3.
    def exitVector3(self, ctx):
        print("exit vector3")

    # Enter a parse tree produced by pbrtParser#sampler.
    def enterSampler(self, ctx):
        print("enter sampler")
        print("->type:" + str(ctx.STRING()))

    # Exit a parse tree produced by pbrtParser#sampler.
    def exitSampler(self, ctx):
        print("exit sampler")

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
        pass

    # Exit a parse tree produced by pbrtParser#lightSource.
    def exitLightSource(self, ctx):
        print("exit lightsource lock")
        pass

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
        pass

    # Exit a parse tree produced by pbrtParser#texture.
    def exitTexture(self, ctx):
        print("exit texture block")
        pass


    # Enter a parse tree produced by pbrtParser#areaLightSource.
    def enterAreaLightSource(self, ctx):
        pass

    # Exit a parse tree produced by pbrtParser#areaLightSource.
    def exitAreaLightSource(self, ctx):
        pass


    # Enter a parse tree produced by pbrtParser#shape.
    def enterShape(self, ctx):
        print("enter shape block")
        pass

    # Exit a parse tree produced by pbrtParser#shape.
    def exitShape(self, ctx):
        print("exit shape block")
        pass


    # Enter a parse tree produced by pbrtParser#material.
    def enterMaterial(self, ctx):
        print("enter material block")
        pass

    # Exit a parse tree produced by pbrtParser#material.
    def exitMaterial(self, ctx):
        print("exit material  block")
        pass


    # Enter a parse tree produced by pbrtParser#include.
    def enterInclude(self, ctx):
        pass

    # Exit a parse tree produced by pbrtParser#include.
    def exitInclude(self, ctx):
        pass


    # Enter a parse tree produced by pbrtParser#worldBlock.
    def enterWorldBlock(self, ctx):
        print("enter world block")
        pass

    # Exit a parse tree produced by pbrtParser#worldBlock.
    def exitWorldBlock(self, ctx):
        print("exit world block")
        pass


    # Enter a parse tree produced by pbrtParser#objectInstance.
    def enterObjectInstance(self, ctx):
        print("enter object block")
        pass

    # Exit a parse tree produced by pbrtParser#objectInstance.
    def exitObjectInstance(self, ctx):
        print("exit object block")
        pass


    # Enter a parse tree produced by pbrtParser#translate.
    def enterTranslate(self, ctx):
        print("enter trnaslate block")
        pass

    # Exit a parse tree produced by pbrtParser#translate.
    def exitTranslate(self, ctx):
        print("exit trnaslate block")
        pass


    # Enter a parse tree produced by pbrtParser#objectBlock.
    def enterObjectBlock(self, ctx):
        print("enter objet block")
        pass

    # Exit a parse tree produced by pbrtParser#objectBlock.
    def exitObjectBlock(self, ctx):
        print("exit objet block")
        pass

    # Enter a parse tree produced by pbrtParser#attributeBlock.
    def enterAttributeBlock(self, ctx):
        print("enter attribut block")
        pass

    # Exit a parse tree produced by pbrtParser#attributeBlock.
    def exitAttributeBlock(self, ctx):
        print("exit attribut block")
        pass


