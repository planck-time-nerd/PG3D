from numpy import array, sin, cos, matmul

ROTATE_Y = lambda A: array([
    [1, 0, 0],
    [0, cos(A), -sin(A)],
    [0, sin(A), cos(A)]
])
ROTATE_Z = lambda A: array([
    [cos(A), 0, sin(A)],
    [0, 1, 0],
    [-sin(A), 0, cos(A)]
])
ROTATE_X = lambda A: array([
    [cos(A), -sin(A), 0],
    [sin(A), cos(A), 0],
    [0, 0, 1]
])

class Camera:
    def __init__(self, position: tuple[int] = (0, 0, 1000), rotation: tuple[float] = (0, 0, 0)) -> None:
        self.x, self.y, self.z = position
        self.rx, self.ry, self.rz = rotation
    def project(self, coord: tuple) -> tuple:
        coord = matmul(
            ROTATE_X(self.rx),
            matmul(
                ROTATE_Y(self.ry),
                matmul(
                    ROTATE_Z(self.rz),
                    array(coord) - array([self.x, self.y, self.z])
                )
            )
        ) + array([self.x, self.y, self.z])
        x, y, z = coord
        constant = self.z / (self.z + z)
        return (x * constant, y * constant)