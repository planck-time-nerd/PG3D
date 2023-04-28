from engine import Window, Event, WASD, K_e, K_DOWN, K_UP, KEYDOWN, K_RIGHT, K_LEFT, get_pressed
from engine.camera import Camera
from engine.objects import WireframeCube

class MainWindow(Window):
    camera = Camera()

    def __init__(self) -> None:
        self.cube = WireframeCube(self.camera, self, (100, 100, 300))
        super().__init__()

    def draw(self):
        held_keys = get_pressed()
        if held_keys[WASD[0]]: self.camera.z += 2
        elif held_keys[WASD[1]]: self.camera.x -= 2
        elif held_keys[WASD[2]]: self.camera.z -= 2
        elif held_keys[WASD[3]]: self.camera.x += 2
        elif held_keys[K_UP]: self.camera.ry += 0.001
        elif held_keys[K_DOWN]: self.camera.ry -= 0.001
        elif held_keys[K_RIGHT]: self.camera.rz += 0.001
        elif held_keys[K_LEFT]: self.camera.rz -= 0.001
        self.cube.draw()
        self.cube.recalculate_vertices()

    def events(self, event: Event):
        if event.type == KEYDOWN:
            if event.key == K_e:
                print("open_inventory")

window = MainWindow()
window.update()