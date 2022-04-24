class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class SourceDetectorPair:
    def __init__(self, source: Coordinate, detector: Coordinate):
        self.source = source
        self.detector = detector
