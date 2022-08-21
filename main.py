from pyglet.math import *
import pyglet

class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # game states
        self.is_paused = False

        # internal stuff
        self.batch = pyglet.graphics.Batch()

    def update(self, dt):
        # update all game objects
        pass

if __name__ == "__main__":
    win = GameWindow(1024, 512, "Physics")

    # run update
    pyglet.clock.schedule_interval(win.update, 1 / 60)

    # display the window and run the app
    pyglet.app.run()
