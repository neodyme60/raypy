import string
from core import texture

from core.spectrum import Spectrum
from core.texture import Texture
from maths.normal import Normal
from maths.point3d import Point3d
from maths.vector3d import Vector3d


class ParamSet():
    def __init__(self):
        self.bools = {}
        self.ints = {}
        self.floats = {}
        self.points = {}
        self.vectors = {}
        self.normals = {}
        self.spectrums = {}
        self.strings = {}
        self.textures = {}

    def reset(self):
        self.bools = {}
        self.ints = {}
        self.floats = {}
        self.points = {}
        self.vectors = {}
        self.normals = {}
        self.spectrums = {}
        self.strings = {}
        self.textures = {}

    def add_bool(self, name: string, values: [bool]):
        if name in self.bools:
            del self.bools[name]
        else:
            self.bools[name] = values

    def add_int(self, name: string, values: [int]):
        if name in self.ints:
            del self.ints[name]
        else:
            self.ints[name] = values

    def add_float(self, name: string, values: [float]):
        if name in self.floats:
            del self.floats[name]
        else:
            self.floats[name] = values

    def add_point(self, name: string, values: [Point3d]):
        if name in self.points:
            del self.points[name]
        else:
            self.points[name] = values

    def add_vector(self, name: string, values: [Vector3d]):
        if name in self.vectors:
            del self.vectors[name]
        else:
            self.vectors[name] = values

    def add_normals(self, name: string, values: [Normal]):
        if name in self.normals:
            del self.normals[name]
        else:
            self.normals[name] = values

    def add_spectrum(self, name: string, values: [Spectrum]):
        if name in self.spectrums:
            del self.spectrums[name]
        else:
            self.spectrums[name] = values

    def add_string(self, name: string, values: [string]):
        if name in self.strings:
            del self.strings[name]
        else:
            self.strings[name] = values

    def add_texture(self, name: string, values: [string]):
        if name in self.textures:
            del self.textures[name]
        else:
            self.textures[name] = values

    def find_float(self, name: string, default: float)->float:
        if name in self.floats:
            return self.floats[name][0]
        return default

    def find_floats(self, name: string)->[float]:
        if name in self.floats:
            return self.floats[name]
        return None

    def find_int(self, name: string, default: int)->int:
        if name in self.ints:
            return self.ints[name][0]
        return default

    def find_ints(self, name: string)->[int]:
        if name in self.ints:
            return self.ints[name]
        return None

    def find_bool(self, name: string, default: bool)->bool:
        if name in self.bools:
            return self.bools[name][0]
        return default

    def find_bools(self, name: string)->[bool]:
        if name in self.bools:
            return self.bools[name]
        return None

    def find_point(self, name: string, default: Point3d)->Point3d:
        if name in self.points:
            return self.points[name][0]
        return None

    def find_points(self, name: string)->Point3d:
        if name in self.points:
            return self.points[name]
        return None

    def find_normal(self, name: string, default: Normal)->Normal:
        if name in self.normals:
            return self.normals[name][0]
        return None

    def find_normals(self, name: string)->Normal:
        if name in self.normals:
            return self.normals[name]
        return None

    def find_vector(self, name: string, default: Vector3d)->Vector3d:
        if name in self.vectors:
            return self.vectors[name][0]
        return None

    def find_vectors(self, name: string)->Vector3d:
        if name in self.vectors:
            return self.vectors[name]
        return None

    def find_spectrum(self, name: string, default: Spectrum)->Spectrum:
        if name in self.spectrums:
            return self.spectrums[name]
        return default

    def find_string(self, name: string, default: string)->string:
        if name in self.strings:
            return self.strings[name]
        return default

    def find_texture(self, name: string)->texture:
        if name in self.textures:
            return self.textures[name]
        else:
            return None

    def find_strings(self, name: string, default: string)->[string]:
        if name in self.strings:
            return self.strings[name]
        return default

    def find_filename(self, name: string, default: string)->string:
        filename = self.find_string(name, "")
        if filename == "":
            return default
        filename = "todo" #AbsolutePath(ResolveFilename(filename))
        return filename
