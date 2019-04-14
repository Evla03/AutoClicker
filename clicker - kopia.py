import mouse
import time
import threading


class Clicker(threading.Thread):
    def __init__(self):
        self.enabled = False
        self.button = None
        self.delay = 0.1
        self.double_click = None
        threading.Thread.__init__(self)
        self._want_abort = False
        self.setDaemon(1)

    def enable(self, button: str, delay: float, double_click: bool=False):
        self.button = button
        self.delay = delay
        self.enabled = True
        self.double_click = double_click
        self.run()

    def disable(self):
        self.enabled = False

    def run(self):
        while not self._want_abort:
            if self.enabled:
                time.sleep(self.delay)
                if self.enabled:
                    # click
                    self.report(True)
                    if not self.double_click:
                        mouse.click(button=self.button)
                    else:
                        mouse.double_click(button=self.button)
            else:
                break

    def abort(self):
        self._want_abort = True

    def report(self, value):
        pass


if __name__ == '__main__':
    clicker = Clicker()
    clicker.enable("left", 1)
