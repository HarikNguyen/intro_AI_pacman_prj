import os
import sys
import math
import random
import string
import time
import types
import tkinter as tk
from PIL import Image, ImageTk

# Define global variables

_is_Windows = sys.platform.startswith("win")  # Check if the OS is Windows

_root_window = None  # The root window for graphics output
_canvas = None  # The canvas which holds graphics
_canvas_xs = None  # Size of canvas object
_canvas_ys = None
_canvas_x = None  # Current position on canvas
_canvas_y = None
_canvas_color = None  # Current colour (set to black below)
_canvas_tsize = 12
_canvas_tserifs = 0

if _is_Windows:
    _canvas_tfonts = ["times new roman", "lucida console"]
else:
    _canvas_tfonts = ["times", "lucidasans-24"]
    pass  # XXX need defaults here


# Define colors
def format_color(r, g, b):
    """Format the color

    Args:
        r (float): Red
        g (float): Green
        b (float): Blue

    Returns:
        str: The formatted color
    """
    return "#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))


def color_to_vector(color):
    """Convert the color to vector

    Args:
        color (str): The color

    Returns:
        list: The list of color vector
    """
    return map(lambda x: int(x, 16) / 256.0, [color[1:3], color[3:5], color[5:7]])


#######################################################################################################
######################################### GRAPHIC FUNCTIONS ###########################################
#######################################################################################################


def graphic_init(width=640, height=480, background_color="black", title=None):
    """Create the graphic window"""
    global _root_window, _canvas, _canvas_xs, _canvas_ys, _canvas_x, _canvas_y, _canvas_color, _canvas_tsize, _canvas_tserifs, _canvas_tfonts

    # Check for duplicate call
    if _root_window is not None:
        # Destroy previous drawing window
        _root_window.destroy()

    # Set up canvas info
    _canvas_xs = width - 1
    _canvas_ys = height - 1
    _canvas_x = 0
    _canvas_y = _canvas_ys
    _canvas_color = background_color

    # Create root window
    _root_window = tk.Tk()
    _root_window.protocol("WM_DELETE_WINDOW", _destroy_window)  # cleanup on exit
    _root_window.title(title or "Pacman Game")
    _root_window.resizable(0, 0)

    # Create canvas object with black background
    try:
        _canvas = tk.Canvas(_root_window, width=width, height=height)
        _canvas.pack()
        draw_background()
        _canvas.update()
    except:
        _root_window = None
        raise EnvironmentError("Error: Unable to create canvas.  Giving up.")


def _destroy_window(event=None):
    """Destroy the window"""
    # Clean up window and exit
    # close root window
    global _root_window
    _root_window.quit()
    _root_window = None


def draw_background():
    """Draw background (background is the polygon)"""
    corners = [(0, 0), (0, _canvas_ys), (_canvas_xs, _canvas_ys), (_canvas_xs, 0)]
    polygon(corners, _canvas_color, _canvas_color, smoothed=False)


def refresh():
    """Refresh screen"""
    _canvas.update_idletasks()  # redraw


def sleep(seconds):
    """Sleep for the given seconds

    Args:
        seconds (float): The seconds to sleep
    """
    global _root_window
    if _root_window == None:
        time.sleep(seconds)
    else:
        _root_window.update_idletasks()
        _root_window.after(int(1000 * seconds), _root_window.quit)
        _root_window.mainloop()


def wait_for_close():
    """Wait for user click x button to close the window or press Esc key"""
    _root_window.bind("<Escape>", _destroy_window)
    _root_window.mainloop()


def bind_esc_to_quit():
    """Bind Esc key to quit the window"""
    _root_window.bind("<Escape>", _destroy_window)


#######################################################################################################
########################################### SHAPE FUNCTIONS ###########################################
################################## Define functions for shape drawing #################################
#######################################################################################################


def matrix_to_screen(mat_point, map_size, grid_size, zoom=1.0):
    """Convert matrix point (row_id, col_id) to screen point (x, y) where x = col_id * grid_size, y = row_id * grid_size"""
    (x, y) = mat_point
    x = (x + 1) * grid_size * zoom
    y = (y + 1) * grid_size * zoom
    screen_point = (x, y)
    return screen_point


def polygon(
    coords, outline_color, fill_color=None, filled=True, smoothed=True, behind=0
):
    """Draw a polygon with the given coordinates.

    Args:
        coords (list): List of coordinates of the polygon (list of tuples)
        outline_color (str): Color of the outline
        fill_color (str, optional): Color of the fill. Defaults to None.
        filled (bool, optional): Whether the polygon is filled. Defaults to True.
        smoothed (bool, optional): Whether the polygon is smoothed. Defaults to True.
        behind (int, optional): The layer of the polygon. Defaults to 0.

    Returns:
        int: The id of the polygon
    """

    # set up info for drawing
    coords_flatten = []
    for coord in coords:
        coords_flatten.append(coord[0])
        coords_flatten.append(coord[1])
    if fill_color == None:
        fill_color = outline_color
    if not filled:
        fill_color = ""

    # create the polygon
    poly = _canvas.create_polygon(
        coords_flatten, outline=outline_color, fill=fill_color, smooth=smoothed, width=2
    )

    if behind > 0:
        _canvas.tag_lower(poly, behind)

    return poly


def circle(
    point_pos,
    radius,
    outline_color,
    fill_color,
    endpoints=None,
    style="pieslice",
    width=2,
):
    """Draw a circle with the given point position and radius

    Args:
        point_pos (tuple): The position of the point
        radius (int): The radius of the circle
        outline_color (str): The color of the outline
        fill_color (str): The color of the fill
        endpoints (tuple, optional): Contain (start and end point). Defaults to None.
        style (str, optional): Type of circle/arc. Defaults to "pieslice".
        width (int, optional): The width of arc. Defaults to 2.

    Returns:
        circle_id (int): The circle canvas object id
    """
    # set up info for drawing
    x, y = point_pos
    # start and end angles for circle arc
    x0, x1 = x - radius - 1, x + radius
    y0, y1 = y - radius - 1, y + radius
    # if endpoints is None, draw a full circle
    if endpoints == None:
        extract_endpoint = [0, 359]
    else:
        extract_endpoint = list(endpoints)
    # if the start angle is greater than the end angle, add 360 to the end angle
    while extract_endpoint[0] > extract_endpoint[1]:
        extract_endpoint[1] += 360

    # create the circle
    circle = _canvas.create_arc(
        x0,
        y0,
        x1,
        y1,
        outline=outline_color,
        fill=fill_color,
        extent=extract_endpoint[1] - extract_endpoint[0],
        start=extract_endpoint[0],
        style=style,
        width=width,
    )

    return circle


def line(start_point, end_point, color=format_color(0, 0, 0), width=2):
    """Draw a line from start_point to end_point

    Args:
        start_point (tuple): The start point
        end_point (tuple): The end point
        color (str, optional): The color of the line. Defaults to format_color(0,0,0).
        width (int, optional): The width of the line. Defaults to 2.

    Returns:
        int: The id of the line canvas object
    """
    x0, y0 = start_point
    x1, y1 = end_point

    line = _canvas.create_line(x0, y0, x1, y1, fill=color, width=width)

    return line


def text(
    position, color, contents, font="Helvetica", size=12, style="normal", anchor="nw"
):
    """The text object"""
    global _canvas_x, _canvas_y
    x, y = position
    font = (font, str(size), style)
    return _canvas.create_text(
        x, y, fill=color, text=contents, font=font, anchor=anchor
    )


def add_2_point(point1, point2):
    """Add 2 points together"""
    return (point1[0] + point2[0], point1[1] + point2[1])


#######################################################################################################
####################################### SHAPE ACTION FUNCTIONS ########################################
################################# Define functions for shape changing #################################
#######################################################################################################


def edit(id, *args):
    """Edit the shape with the given id

    Args:
        id (int): The id of the shape
    """
    _canvas.itemconfigure(id, **dict(args))


def change_color(id, new_color):
    """Change the color of the shape with the given id"""
    _canvas.itemconfigure(id, fill=new_color)


def change_text(id, new_text, font=None, size=12, style="normal"):
    """Change the content of the text with the given id"""
    _canvas.itemconfigure(id, text=new_text)
    if font != None:
        _canvas.itemconfigure(id, font=(font, "-%d" % size, style))


def move_to(
    object,
    x,
    y=None,
    d_o_e=lambda arg: _root_window.dooneevent(arg),
    d_w=tk._tkinter.DONT_WAIT,
):
    """Move the object to the given position (from current to x, y)
    Meaning that the object will move to (x, y)

    Args:
        object (int): The id of the object
        x (int): The x coordinate
        y (int, optional): The y coordinate. Defaults to None.
        d_o_e (function, optional): The function to do one event. Defaults to lambda arg: _root_window.dooneevent(arg).
        d_w (int, optional): The wait time. Defaults to tk._tkinter.DONT_WAIT.
    Raises:
        ValueError: Incomprehensible coordinates

    """
    if y is None:
        try:
            x, y = x
        except:
            raise ValueError("Incomprehensible coordinates")

    is_horizontal = True
    new_coords = []
    current_x, current_y = _canvas.coords(object)[0:2]  # first point
    for coord in _canvas.coords(object):
        if is_horizontal:
            inc = x - current_x
        else:
            inc = y - current_y
        is_horizontal = not is_horizontal

        new_coords.append(coord + inc)

    _canvas.coords(object, *new_coords)
    d_o_e(d_w)


def move_by(
    object,
    x,
    y=None,
    d_o_e=lambda arg: _root_window.dooneevent(arg),
    d_w=tk._tkinter.DONT_WAIT,
    lift=False,
):
    """Move the object by the given position (from current by x, y)
    Meaning that the object will move to (current_x + x, current_y + y)

    Args:
        object (int): Object id
        x (int or tuple of int): The x coordinate or the tuple of x and y coordinate
        y (int or None, optional): The y coordinate. Defaults to None.
        lift (bool, optional): The flag to lift the object. Defaults to False.

    Raises:
        Exception: Incomprehensible coordinates
    """
    if y is None:
        try:
            x, y = x
        except:
            raise Exception("Incomprehensible coordinates")
    is_horizontal = True
    new_coords = []
    for coord in _canvas.coords(object):
        if is_horizontal:
            inc = x
        else:
            inc = y
        is_horizontal = not is_horizontal

        new_coords.append(coord + inc)

    # Update the object
    _canvas.coords(object, *new_coords)

    # Update the canvas
    d_o_e(d_w)
    if lift:
        _canvas.tag_raise(object)


def move_circle(
    id,
    center_point,
    radius,
    endpoints=None,
):
    """Move the circle with the given id to the given center point and radius"""
    x, y = center_point
    x0, y0 = x - radius - 1, y - radius - 1  # -1 to make sure the circle is not cut off
    x1, y1 = x + radius, y + radius

    # if endpoints is None, draw a full circle
    if endpoints == None:
        extract_endpoint = [0, 359]
    else:
        extract_endpoint = list(endpoints)
    # if the start angle is greater than the end angle, add 360 to the end angle
    while extract_endpoint[0] > extract_endpoint[1]:
        extract_endpoint[1] += 360

    # Update the circle
    edit(
        id,
        ("start", extract_endpoint[0]),
        ("extent", extract_endpoint[1] - extract_endpoint[0]),
    )

    # Move to x0, y0
    move_to(id, x0, y0)


def remove_from_screen(
    id,
    d_o_e=lambda arg: _root_window.dooneevent(arg),
    d_w=tk._tkinter.DONT_WAIT,
):
    """Remove the shape with the given id from the screen"""
    _canvas.delete(id)
    d_o_e(d_w)
