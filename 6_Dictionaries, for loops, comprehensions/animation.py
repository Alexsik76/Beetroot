from asciimatics.effects import RandomNoise  # $ pip install asciimatics
from asciimatics.renderers import SpeechBubble, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError


def demo(screen):
    render = Rainbow(screen, SpeechBubble('Hello Alex'))
    effects = [RandomNoise(screen, signal=render)]
    screen.play([Scene(effects, -1)], stop_on_resize=True)


while True:
    try:
        Screen.wrapper(demo)
        break
    except ResizeScreenError:
        pass
