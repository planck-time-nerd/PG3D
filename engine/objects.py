from pygame.draw import line
from numpy import array

class Wireframe:
    stroke_color = "#f55442"
    stroke_width = 2

    def __init__(self, camera, canvas, vertexTable, edgeRelation: list[tuple]) -> None:
        self.camera = camera
        self.canvas = canvas
        self.vertices = vertexTable
        self.edges = edgeRelation
    def project(self):
        projected = []
        for vertex in self.vertices:
            projected.append(self.camera.project(vertex))
        for line in self.edges:
            yield projected[line[0]], projected[line[1]]
    def draw(self):
        for coordA, coordB in self.project():
            line(self.canvas.screen, self.stroke_color, coordA, coordB, self.stroke_width)

class WireframeCube(Wireframe):
    def __init__(self, camera, canvas, position: tuple[float] = (100, 100, 100), sideLength: int = 100) -> None:
        self.sideLength = sideLength
        self.x, self.y, self.z = position
        self.camera = camera
        self.edges = [
            (0,1),(1,2),(2,3),(3,0),
            (4,5),(5,6),(6,7),(7,4),
            (4,3),(5,0),(6,1),(7,2)
        ]
        self.recalculate_vertices()
        super().__init__(camera, canvas, self.vertices, self.edges)
    def recalculate_vertices(self):
        self.vertices = self.sideLength * array([
            [0,0,0],
            [1,0,0],
            [1,1,0],
            [0,1,0],
            [0,1,1],
            [0,0,1],
            [1,0,1],
            [1,1,1]
        ]) + array([
            [self.x - self.camera.x, self.y - self.camera.y, self.z - self.camera.z]
        ] * 8)