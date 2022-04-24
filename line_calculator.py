from model import Coordinate


class BresenhamLineCalculator:
    def __init__(self):
        pass

    @staticmethod
    def calculate_between(start: Coordinate, end: Coordinate):
        dx = abs(end.x - start.x)
        dy = abs(end.y - start.y)

        if dx > dy:
            return BresenhamLineCalculator._plot_pixel(start.x, start.y, end.x, end.y, dx, dy, False)
        else:
            return BresenhamLineCalculator._plot_pixel(start.y, start.x, end.y, end.x, dy, dx, True)

    @staticmethod
    def _plot_pixel(x1: int, y1: int, x2: int, y2: int, dx: int, dy: int, revert: bool):
        pk = 2 * dy - dx
        for _ in range(dx + 1):
            if revert:
                yield Coordinate(y1, x1)
            else:
                yield Coordinate(x1, y1)

            if x1 < x2:
                x1 += 1
            else:
                x1 -= 1

            if pk < 0:
                pk = pk + 2 * dy
            else:
                if y1 < y2:
                    y1 += 1
                else:
                    y1 -= 1
                pk = pk + 2 * dy - 2 * dx