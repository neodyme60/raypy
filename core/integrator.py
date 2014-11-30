from core.bsdf import BSDF, BSDFSampleOffsets, BSDFSample
from core.bxdf import BxDFType
from core.camera import Camera
from core.light import Light
from core.light_sample import LightSample
from core.light_sample_offsets import LightSampleOffsets
from core.monte_carlo import PowerHeuristic
from core.renderer import Renderer
from core.sample import Sample
from core.sampler import Sampler
from core.scene import Scene
from core.spectrum import Spectrum
from core.visibility_tester import VisibilityTester
from maths.normal import Normal
from maths.point3d import Point3d
from maths.vector3d import Vector3d


class Integrator():
    def __init__(self):
        pass

    def Preprocess(self, scene: Scene, camera: Camera, renderer: Renderer):
        pass

    def RequestSamples(self, sampler: Sampler, sample: Sample, scene: Scene):
        pass


def UniformSampleAllLights(scene: Scene, renderer: Renderer, p: Point3d, n: Normal, wo: Vector3d,
                           rayEpsilon: float, time: float, bsdf: BSDF, sample: Sample,
                           lightSampleOffsets: [LightSampleOffsets],
                           bsdfSampleOffsets: [BSDFSampleOffsets]) -> Spectrum:
    L = Spectrum(0.0)
    for i in range(len(scene.lights)):
        light = scene.lights[i]
        if lightSampleOffsets == None:
            nSamples = 1
        else:
            nSamples = lightSampleOffsets[i].nSamples

        # Estimate direct lighting from _light_ samples
        Ld = Spectrum(0.0)

        for j in range(nSamples):
            # Find light and BSDF sample values for direct lighting estimate
            if (lightSampleOffsets != None and bsdfSampleOffsets != None):
                lightSample = LightSample.create_from_sample(sample, lightSampleOffsets[i], j)
                bsdfSample = BSDFSample.create_from_sample(sample, bsdfSampleOffsets[i], j)
            else:
                lightSample = LightSample.create_from_random()
                bsdfSample = BSDFSample.create_from_random()
            Ld += EstimateDirect(scene, renderer, light, p, n, wo, rayEpsilon, time, bsdf, lightSample, bsdfSample,
                                 BxDFType.BSDF_ALL & ~BxDFType.BSDF_SPECULAR)
        L += Ld*1.0 / nSamples
    return L


def UniformSampleOneLight(scene: Scene, renderer: Renderer, Point3d, n: Normal, wo: Vector3d,
                          rayEpsilon: float, time: float, bsdf: BSDF, sample: Sample,
                          lightSampleOffsets: [LightSampleOffsets], bsdfSampleOffsets: [BSDFSampleOffsets],
                          lightNumOffset: int=-1) -> Spectrum:
    L = Spectrum(0.0)
    return L


def EstimateDirect(scene: Scene, renderer: Renderer, light: Light, p: Point3d, n: Normal, wo: Vector3d,
                   rayEpsilon: float, time: float, bsdf: BSDF, lightSample: LightSample, bsdfSample: BSDFSample,
                   BxDFTypeFlag: int) -> Spectrum:
    Ld = Spectrum(0.0)

    # Sample light source with multiple importance sampling
    bsdfPdf = 0.0

    visibility = VisibilityTester()
    wi, Li, lightPdf = light.Sample_L1(p, rayEpsilon, lightSample, time, visibility)
    if lightPdf > 0.0 and not Li.get_is_black():
        f = bsdf.f(wo, wi, BxDFTypeFlag)
        if not f.get_is_black() and visibility.Unoccluded(scene):
            # Add light's contribution to reflected radiance
#            Li *= visibility.Transmittance(scene, renderer, None)
            inv_lightPdf = 1.0/ lightPdf
            if light.get_is_delta_light():
                inv_lightPdf = 1.0/ lightPdf
                Ld += f * Li * (abs(Vector3d.dot(wi, n)) * inv_lightPdf)
            else:
                bsdfPdf = bsdf.get_Pdf(wo, wi, BxDFTypeFlag)
                weight = PowerHeuristic(1, lightPdf, 1, bsdfPdf)
                Ld += f * Li * (abs(Vector3d.dot(wi, n)) * weight * inv_lightPdf)

    # Sample BSDF with multiple importance sampling
#    if not light.get_is_delta_light():
#        f = bsdf.Sample_f(wo, &wi, bsdfSample, &bsdfPdf, flags, &sampledType);
#        if not f.IsBlack() and bsdfPdf > 0.0:
#            weight = 1.0
#            if not (sampledType & BSDF_SPECULAR):
#                lightPdf = light.Pdf(p, wi)
#                if lightPdf == 0.0:
#                        return Ld
#                weight = PowerHeuristic(1, bsdfPdf, 1, lightPdf)

    # Add light contribution from BSDF sampling
    #            Intersection lightIsect;
    #            Li = Spectrum(0.0)
    #            RayDifferential ray(p, wi, rayEpsilon, INFINITY, time)
    #            if (scene->Intersect(ray, &lightIsect)):
    #                if (lightIsect.primitive->GetAreaLight() == light):
    #                    Li = lightIsect.Le(-wi);
    #            else:
    #                Li = light.Le(ray)
    #            if !Li.IsBlack():
    #                Li *= renderer.Transmittance(scene, ray, NULL, rng, arena)
    #                Ld += f * Li * AbsDot(wi, n) * weight / bsdfPdf
    return Ld
