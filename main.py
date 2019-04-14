import wx
from ui.wxUI import EventedUIFrame, UICredits
from clicker import Clicker

buttons = ("left", "right", "middle")
units = (1000, 1, 1 / 60, 1 / 3600)


def parse_float(value):
    try:
        value = value.replace(",", ".")
        return float(value)
    except ValueError as e:
        return False


class ScriptedEventedUIFrame(EventedUIFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clicker = Clicker()
        self.delay = float(self.input_delay.Value)
        self.credit_frame = EventedUICredits(self)

    def enable_clicker(self, event):
        if event.IsChecked():
            self.button_start.SetLabel(f"[{self.button_start.GetLabel()}]")
            button = buttons[self.button_select_choice.GetSelection()]
            delay = self.delay / units[self.timeunit_choice.GetSelection()]
            double_click = self.check_double.IsChecked()
            self.input_delay.SetLabel(str(self.delay))
            self.clicker.enable(button, delay, double_click)
        else:
            self.clicker.disable()
            self.button_start.SetLabel(self.button_start.GetLabel().replace("[", "").replace("]", ""))

    def quit_program(self, event):
        self.clicker.disable()
        quit()

    def time_text_change(self, event):
        value = parse_float(event.GetString())
        if value:
            self.delay = value

    def time_text_enter(self, event):
        value = parse_float(event.GetString())
        if value:
            self.delay = value
            # set event's string to the value
            self.input_delay.SetLabel(str(self.delay))

    def show_credits(self, event):
        self.credit_frame.Show()


class EventedUICredits(UICredits):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def close_credits(self, event):
        self.Close()


class MainApp(wx.App):
    """Class Main App."""

    def OnInit(self):
        """Init Main App."""
        self.frame = ScriptedEventedUIFrame(None)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True


def main():
    app = MainApp(0)
    app.MainLoop()


if __name__ == '__main__':
    main()
