import mouse
import threading


class Clicker():
    def __init__(self):
        self.enabled = False
        self.button = None
        self.delay = 0.1
        self.double_click = None

    def enable(self, button: str, delay: float, double_click: bool=False):
        self.button = button
        self.delay = delay
        self.enabled = True
        self.double_click = double_click
        self.timer = threading.Timer(self.delay, self.tick)
        self.timer.start()

    def disable(self):
        self.enabled = False

    def tick(self):
        if self.enabled:
            if self.enabled:
                # click
                self.report(True)
                if not self.double_click:
                    mouse.click(button=self.button)
                else:
                    mouse.double_click(button=self.button)
                self.timer = threading.Timer(self.delay, self.tick)
                self.timer.start()

    def report(self, value):
        pass


if __name__ == '__main__':
    clicker = Clicker()
    clicker.enable("left", 1)
