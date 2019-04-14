if __name__ != '__main__':
    import wx
    from .UIBase import *
else:
    raise ImportError("This must be imported and can not be ran directly.")


class EventedUIFrame(UIFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EventedUIHotkeys:
    def done(self):
        self.close()


def main():
    app = wx.App()
    frame = EventedUIFrame(None)
    frame.Show()
    app.MainLoop()
    return frame
