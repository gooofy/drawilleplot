import io
from drawille import Canvas
from PIL import Image

from matplotlib._pylab_helpers import Gcf
from matplotlib.backend_bases import (
    _Backend, FigureCanvasBase, FigureManagerBase, RendererBase)
from matplotlib.backends.backend_agg import RendererAgg, FigureCanvasAgg

class RendererDrawille(RendererAgg):

    def __init__(self, width, height, dpi):
        super(RendererDrawille, self).__init__(width, height, dpi)
        self.texts = []

    def clear(self):
        super(RendererDrawille, self).clear()
        self.texts = []
       
    def draw_text(self, gc, x, y, s, prop, angle, ismath=False, mtext=None):
        # super(RendererDrawille, self).draw_text(gc, x, y, s, prop, angle, ismath=ismath, mtext=mtext)
        self.texts.append((x,y,s))


def show():
    try:
        for manager in Gcf.get_all_fig_managers():
            canvas = manager.canvas
            canvas.draw()
            string = canvas.to_txt()
            print(string)
            # display(HTML("<div style=\"font-size:2px; line-height:90%;\"><tt>" + string + "</tt></div>"))
    finally:
        #if close and Gcf.get_all_fig_managers():
        #    matplotlib.pyplot.close('all')
        pass

class FigureCanvasDrawille(FigureCanvasAgg):

    def get_renderer(self, cleared=False):
        l, b, w, h = self.figure.bbox.bounds
        key = w, h, self.figure.dpi
        reuse_renderer = (hasattr(self, "renderer")
                          and getattr(self, "_lastKey", None) == key)
        if not reuse_renderer:
            self.renderer = RendererDrawille(w, h, self.figure.dpi)
            self._lastKey = key
        elif cleared:
            self.renderer.clear()
        return self.renderer

    def to_txt(self, sep="\n", tw=240, invert=False, threshold=200):
        # import pdb; pdb.set_trace()

        buf = io.BytesIO()
        self.print_png(buf)
        buf.seek(0)

        i = Image.open(buf)

        w, h = i.size

        ratio = tw / float(w)
        w = tw
        h = int(h * ratio)
        i = i.resize((w, h), Image.LANCZOS)

        i = i.convert(mode="L")

        can = Canvas()

        for y in range(h):
            for x in range(w):

                pix = i.getpixel((x,y))

                if invert:
                    if pix > threshold:
                        can.set(x, y)
                else:
                    if pix < threshold:
                        can.set(x, y)

        for x,y,s in self.renderer.texts:
            can.set_text(int(x*ratio), int(y*ratio), s)

        return can.frame()

FigureCanvas = FigureCanvasDrawille
FigureManager = FigureManagerBase

