import string

from core.param_set_item import ParamSetItem
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

    def add_bool(self, name: string, value: bool):
        if name in self.bools:
            del self.bools[name]
        else:
            self.bools[name] = ParamSetItem(name, value)

    def add_int(self, name: string, value: int):
        if name in self.ints:
            del self.ints[name]
        else:
            self.ints[name] = ParamSetItem(name, value)

    def add_float(self, name: string, value: float):
        if name in self.floats:
            del self.floats[name]
        else:
            self.floats[name] = ParamSetItem(name, value)

    def add_point(self, name: string, value: Point3d):
        if name in self.floats:
            del self.floats[name]
        else:
            self.floats[name] = ParamSetItem(name, value)

    def add_vector(self, name: string, value: Vector3d):
        if name in self.vectors:
            del self.vectors[name]
        else:
            self.vectors[name] = ParamSetItem(name, value)

    def add_normals(self, name: string, value: Normal):
        if name in self.normals:
            del self.normals[name]
        else:
            self.normals[name] = ParamSetItem(name, value)

    def add_spectrum(self, name: string, value: Spectrum):
        if name in self.spectrums:
            del self.spectrums[name]
        else:
            self.spectrums[name] = ParamSetItem(name, value)

    def add_string(self, name: string, value: string):
        if name in self.strings:
            del self.strings[name]
        else:
            self.strings[name] = ParamSetItem(name, value)

    def add_texture(self, name: string, value: Texture):
        if name in self.textures:
            del self.textures[name]
        else:
            self.textures[name] = ParamSetItem(name, value)

    def find_float(self, name: string):
        if name in self.floats:
            return self.floats[name]
        return None

    def find_int(self, name: string):
        if name in self.ints:
            return self.ints[name]
        return None

    def find_bool(self, name: string):
        if name in self.bools:
            return self.bools[name]
        return None

    def find_point(self, name: string):
        if name in self.points:
            return self.points[name]
        return None

    def find_normal(self, name: string):
        if name in self.normals:
            return self.normals[name]
        return None

    def find_vector(self, name: string):
        if name in self.vectors:
            return self.vectors[name]
        return None

    def find_spectrum(self, name: string):
        if name in self.spectrums:
            return self.spectrums[name]
        return None

    def find_string(self, name: string):
        if name in self.strings:
            return self.strings[name]
        return None

    def find_texture(self, name: string):
        if name in self.textures:
            return self.textures[name]
        return None