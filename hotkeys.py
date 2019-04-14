import keyboard


class Hotkey:
    def __init__(self, function, key="F6"):
        self.function = function
        self.key = key
        self.toggled = False
        keyboard.on_press_key(key, self.on_pressed, True)

    def on_pressed(self, event):
        self.toggled = not self.toggled
        if self.toggled:
            self.function()
