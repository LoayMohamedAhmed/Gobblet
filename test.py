import tkinter as tk
from start import *
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill=tk.BOTH,expand=True)


if __name__ == "__main__":
    app = SampleApp()
    app.configure(background="black")
    app.geometry("1500x800")
    app.resizable(0,0)
    app.mainloop()
