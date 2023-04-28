from pygame.display import set_mode, flip as refresh_screen
from pygame import init, QUIT, quit as quit_pg, KEYDOWN, K_w, K_s, K_a, K_d, K_e, K_UP, K_DOWN, K_RIGHT, K_LEFT
from pygame.event import get as get_events, Event
from pygame.time import Clock
from pygame.key import get_pressed

WASD: tuple = (K_w, K_a, K_s, K_d)

class Window:
    running  = True
    clock    = Clock()
    fps      = 60
    bg_color = "#1a1a1a"

    def __init__(self, geometry: tuple[int] = (800, 600)) -> None:
        self.screen = set_mode(geometry)

    def update(self):
        while self.running:
            for event in get_events():
                if event.type == QUIT:
                    self.running = False
                self.events(event)

            self.screen.fill(self.bg_color)
            self.draw()
            refresh_screen()
            self.clock.tick(self.fps)
        quit_pg()