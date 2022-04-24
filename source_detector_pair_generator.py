from model import Coordinate, SourceDetectorPair
from math import sin, cos, radians


class SourceDetectorPairGenerator:
    def __init__(self, scan_height, pair_count: int, spread: int, step: int):
        self._radius = scan_height / 2
        self._pair_count = pair_count
        self._spread = spread if pair_count > 1 else 0
        self._step = step

    def generate(self, iteration: int) -> list:
        pair_degree_difference = self._spread / self._pair_count
        source_degree = 90 - (pair_degree_difference * (self._pair_count - 1) / 2) - (iteration * self._step)
        detector_degree = -90 + (pair_degree_difference * (self._pair_count - 1) / 2) - (iteration * self._step)
        pairs = []

        for pair in range(self._pair_count):
            source = Coordinate(
                int(self._radius + self._radius * self._cos(source_degree)),
                int(self._radius + self._radius * self._sin(source_degree))
            )
            detector = Coordinate(
                int(self._radius + self._radius * self._cos(detector_degree)),
                int(self._radius + self._radius * self._sin(detector_degree))
            )
            pairs.append(SourceDetectorPair(source, detector))

            source_degree += pair_degree_difference
            detector_degree -= pair_degree_difference

        return pairs

    @staticmethod
    def _cos(angle: float):
        if angle % 360 == 0:
            return 1 if angle > 0 else -1

        if angle % 270 == 0:
            return 0

        if angle % 180 == 0:
            return -1 if angle > 0 else 1

        if angle % 90 == 0:
            return 0

        return cos(radians(angle))

    @staticmethod
    def _sin(angle: float):
        if angle % 360 == 0:
            return 0

        if angle % 270 == 0:
            return -1 if angle > 0 else 1

        if angle % 180 == 0:
            return 0

        if angle % 90 == 0:
            return 1 if angle > 0 else -1

        return sin(radians(angle))
