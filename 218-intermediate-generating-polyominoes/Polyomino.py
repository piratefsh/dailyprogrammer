import numpy as np
import math
import bisect
from copy import deepcopy


class Polyomino():
    # Constructs a Polyomino on a canvas that can accomodate max size,
    # which is sixe x size

    def __init__(self, size):
        self.size = size
        self.coords = set()
        self.fingerprint = None

    # Returns coordinates of all open sides

    def has_tile(coord):
        return coord in self.coords

    def open_sides(self):
        coords = []
        for c in self.coords:
            x, y = c[0], c[1]
            if (x-1, y) not in self.coords:
                coords.append((x-1, y))
            if (x+1, y) not in self.coords:
                coords.append((x+1, y))
            if (x, y-1) not in self.coords:
                coords.append((x, y-1))
            if (x, y+1) not in self.coords:
                coords.append((x, y+1))
        return coords

    def set(self, coords):
        self.coords.add(coords)
        return self

    def set_coords(self, coords):
        self.coords = set(coords)
        return self

    def identical(self, other):
        return self.coords == other.coords

    def normalized_coords(self):
        min_x = min(self.coords, key=lambda x: x[0])[0]
        min_y = min(self.coords, key=lambda x: x[1])[1]
        return [(x-min_x, y-min_y) for x, y in self.coords]

    # normalize self
    def normalize(self):
        self.set_coords(self.normalized_coords())
        return self

    # return version of normalized self
    def normalized(self):
        normalized_coords = self.normalized_coords()
        p = Polyomino(self.size).set_coords(normalized_coords)
        return p

    # get reflection of self
    def reflections(self):
        p = Polyomino(self.size).set_coords(
            [(y, x) for x, y in self.coords]).normalize()
        return [p]

    # get possible rotations of self
    def rotations(self):
        rotations = []
        rotated_coords = self.coords
        for _ in range(3):
            rotated_coords = [(-y, x) for x, y in rotated_coords]
            rotations.append(
                Polyomino(self.size).set_coords(rotated_coords).normalize())
        return rotations

    def get_fingerprint(self):
        if self.fingerprint is None:
            reflections = self.reflections()
            rotated_reflections = sum(
                map(lambda x: x.rotations(), reflections), [])
            incarnations = [
                self.normalized()] + self.reflections()
                + self.rotations() + rotated_reflections
            coords = [x.coords for x in incarnations]
            coords.sort(key=lambda x: str(sorted(list(x))))
            self.fingerprint = str(sorted(coords[0]))
        return self.fingerprint

    # Check equality of this poly to another
    def __eq__(self, other):
        return self.get_fingerprint() == other.get_fingerprint()

    def __hash__(self):
        return hash(self.get_fingerprint())

    def __repr__(self):
        string = ""
        for x in range(self.size):
            for y in range(self.size):
                string += '# ' if (x, y) in self.coords else '. '
            string += "\n"
        return string
