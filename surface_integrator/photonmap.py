import math
from scipy.spatial.ckdtree import cKDTree
from core.camera import Camera
from core.intersection import Intersection
from core.ray import Ray
from core.renderer import Renderer
from core.sample import Sample
from core.sampler import Sampler
from core.scene import Scene
from core.spectrum import Spectrum
from core.surface_integrator import SurfaceIntegrator
from maths.point3d import Point3d
from maths.vector3d import Vector3d


class Photon():
    def __init__(self, p: Point3d, alpha: Spectrum, wi: Vector3d):
        self.p = p
        self.alpha = alpha
        self.wi = wi

class KdTreePhoton:
    def __init__(self):
        self.tree = None

# PhotonIntegrator Local Declarations
class PhotonIntegrator(SurfaceIntegrator):

    def __init__(self, ncaus: int, nind: int, nl: int, mdepth: int, mphodepth: int, mdist: float, fg: bool, gs: int, ga: float):
        super().__init__()
        self.nCausticPhotonsWanted = ncaus
        self.nIndirectPhotonsWanted = nind
        self.nLookup = nl
        self.maxSpecularDepth = mdepth
        self.maxPhotonDepth = mphodepth
        self.maxDistSquared = mdist * mdist
        self.finalGather = fg
        self.cosGatherAngle = math.cos(math.radians(ga))
        self.gatherSamples = gs
        self.nCausticPaths = 0
        self.nIndirectPaths = 0
        self.lightSampleOffsets = None
        self.bsdfSampleOffsets = None
        self.causticMap = KdTreePhoton()
        self.indirectMap = KdTreePhoton()
        self.radianceMap = KdTreePhoton()

    def Li(self, scene, renderer: Renderer, ray: Ray, intersection: Intersection, sample: Sample) -> Spectrum:
        return super().Li(scene, renderer, ray, intersection, sample)

    def Preprocess(self, scene: Scene, camera: Camera, renderer: Renderer):
        super().Preprocess(scene, camera, renderer)

    def RequestSamples(self, sampler: Sampler, sample: Sample, scene: Scene):
        super().RequestSamples(sampler, sample, scene)



