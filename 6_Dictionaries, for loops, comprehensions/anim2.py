from asciimatics.screen import ManagedScreen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from time import sleep


@ManagedScreen
def demo(screen=None):
    screen.print_at('Hello world!', 0, 0, colour=4, attr=3)
    screen.refresh()
    sleep(1)


demo()
