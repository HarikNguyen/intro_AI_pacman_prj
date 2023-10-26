"""Supporting functions for the graphic module.
"""

import sys
import time
import tkinter


_Windows = sys.platform == "win32"  # True if on Win95/98/NT

_root_window = None  # The root window for graphics output
_canvas = None  # The canvas which holds graphics
_canvas_xs = None  # Size of canvas object
_canvas_ys = None
_canvas_x = None  # Current position on canvas
_canvas_y = None
_canvas_col = None  # Current colour (set to black below)
_canvas_tsize = 12
_canvas_tserifs = 0


def formatColor(r, g, b):
    return "#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))


def colorToVector(color):
    return list(map(lambda x: int(x, 16) / 256.0, [color[1:3], color[3:5], color[5:7]]))


# define font
if _Windows:
    _canvas_tfonts = ["times new roman", "lucida console"]
else:
    _canvas_tfonts = ["times", "lucidasans-24"]
    pass  # XXX need defaults here


def sleep(secs):
    global _root_window
    if _root_window == None:
        time.sleep(secs)
    else:
        _root_window.update_idletasks()
        _root_window.after(int(1000 * secs), _root_window.quit)
        _root_window.mainloop()


def begin_graphics(width=640, height=480, color=formatColor(0, 0, 0), title=None):

    global _root_window, _canvas, _canvas_x, _canvas_y, _canvas_xs, _canvas_ys, _bg_color

    # Check for duplicate call
    if _root_window is not None:
        # Lose the window.
        _root_window.destroy()

    # Save the canvas size parameters
    _canvas_xs, _canvas_ys = width - 1, height - 1
    _canvas_x, _canvas_y = 0, _canvas_ys
    _bg_color = color

    # Create the root window
    _root_window = tkinter.Tk()
    _root_window.protocol("WM_DELETE_WINDOW", _destroy_window)
    _root_window.title(title or "Graphics Window")
    _root_window.resizable(0, 0)

    # Create the canvas object
    try:
        _canvas = tkinter.Canvas(_root_window, width=width, height=height)
        _canvas.pack()
        draw_background()
        _canvas.update()
    except:
        _root_window = None
        raise


def _destroy_window(event=None):
    sys.exit(0)


def draw_background():
    corners = [(0, 0), (0, _canvas_ys), (_canvas_xs, _canvas_ys), (_canvas_xs, 0)]
    polygon(corners, _bg_color, fillColor=_bg_color, filled=True, smoothed=False)


def end_graphics():
    global _root_window, _canvas, _mouse_enabled
    try:
        try:
            sleep(1)
            if _root_window != None:
                _root_window.destroy()
        except SystemExit as e:
            print("Ending graphics raised an exception:", e)
    finally:
        _root_window = None
        _canvas = None
        _mouse_enabled = 0


def clear_screen(background=None):
    global _canvas_x, _canvas_y
    _canvas.delete("all")
    draw_background()
    _canvas_x, _canvas_y = 0, _canvas_ys


def polygon(
    coords, outlineColor, fillColor=None, filled=1, smoothed=1, behind=0, width=1
):
    c = []
    for coord in coords:
        c.append(coord[0])
        c.append(coord[1])
    if fillColor == None:
        fillColor = outlineColor
    if filled == 0:
        fillColor = ""
    poly = _canvas.create_polygon(
        c, outline=outlineColor, fill=fillColor, smooth=smoothed, width=width
    )
    if behind > 0:
        _canvas.tag_lower(poly, behind)  # Higher should be more visible
    return poly


def square(pos, r, color, filled=1, behind=0):
    x, y = pos
    coords = [(x - r, y - r), (x + r, y - r), (x + r, y + r), (x - r, y + r)]
    return polygon(coords, color, color, filled, 0, behind=behind)


def circle(
    pos, r, outlineColor, fillColor=None, endpoints=None, style="pieslice", width=2
):
    x, y = pos
    x0, x1 = x - r - 1, x + r
    y0, y1 = y - r - 1, y + r
    if endpoints == None:
        e = [0, 359]
    else:
        e = list(endpoints)
    while e[0] > e[1]:
        e[1] = e[1] + 360

    return _canvas.create_arc(
        x0,
        y0,
        x1,
        y1,
        outline=outlineColor,
        fill=fillColor or outlineColor,
        extent=e[1] - e[0],
        start=e[0],
        style=style,
        width=width,
    )


def image(pos, file="../../blueghost.gif"):
    x, y = pos
    # img = PhotoImage(file=file)
    return _canvas.create_image(
        x, y, image=tkinter.PhotoImage(file=file), anchor=tkinter.NW
    )


def refresh():
    _canvas.update_idletasks()


def edit(id, *args):
    _canvas.itemconfigure(id, **dict(args))


def text(pos, color, contents, font="Helvetica", size=12, style="normal", anchor="nw"):
    global _canvas_x, _canvas_y
    x, y = pos
    font = (font, str(size), style)
    return _canvas.create_text(
        x, y, fill=color, text=contents, font=font, anchor=anchor
    )


def changeText(id, newText, font=None, size=12, style="normal"):
    _canvas.itemconfigure(id, text=newText)
    if font != None:
        _canvas.itemconfigure(id, font=(font, "-%d" % size, style))


def changeColor(id, newColor):
    _canvas.itemconfigure(id, fill=newColor)


def line(here, there, color=formatColor(0, 0, 0), width=2):
    x0, y0 = here[0], here[1]
    x1, y1 = there[0], there[1]
    return _canvas.create_line(x0, y0, x1, y1, fill=color, width=width)
