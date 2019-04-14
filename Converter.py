"""Coordinates conversion from from WGS84 coordinates to L-Est97 and vice versa."""
from pyproj import Proj
from tkinter import *
from tkinter import ttk

p1 = Proj(init='epsg:3301', preserve_units=False)

def calculate():
    """
    Calls conversion functions and writes the answer into the GUI
    :return:
    """
    try:
        x = float(xInput.get())
        y = float(yInput.get())
        (y, x) = est_to_wgs(x, y)
    except ValueError:
        x = xInput.get()
        y = yInput.get()
        (y, x) = wgs_to_est(x, y)
    answer1.set(x)
    answer2.set(y)

def wgs_to_est(x,y):
    """
    Converts from WGS84 to L-Est97
    :param x: WGS84 latitude to convert
    :param y: WGS84 longitude to convert
    :return: coordinates in L-Est97
    """
    xdeg = float(x.split('°')[0])
    xmin = float(x.split('°')[1].split("'")[0])
    xsek = float(x.split("'")[1].split('"')[0])
    ydeg = float(y.split('°')[0])
    ymin = float(y.split('°')[1].split("'")[0])
    ysek = float(y.split("'")[1].split('"')[0])
    x, y = degrees_to_decimal(xdeg, xmin, xsek), degrees_to_decimal(ydeg, ymin, ysek)
    y, x = p1(y, x)
    return y, x

def est_to_wgs(x,y):
    """
    Converts from L-Est97 to WGS84
    :param x: L-Est97 X-axe direction is to North
    :param y: L-Est97 Y-axe direction is to East
    :return: coordinates in WGS84
    """
    (x, y) = p1(y, x, inverse=True)
    return decimal_to_degrees(x), decimal_to_degrees(y)

def decimal_to_degrees(decimal):
    """
    Converts decimal numbers to degrees, minutes and seconds and formats it with appropriate symbols
    :param decimal: Coordinate in decimal number
    :return: Coordinate in degrees, minutes and seconds
    """
    degrees = int(decimal)
    minutes = int((decimal - degrees) * 60)
    seconds = round((decimal - degrees - minutes / 60.) * 3600, 4)
    return "".join(map(str, [degrees, '° ', minutes, "' ", seconds, '"']))

def degrees_to_decimal(degrees, minutes, seconds):
    """
    Converts degrees, minutes and seconds to decimal numbers
    :param degrees:
    :param minutes:
    :param seconds:
    :return: Decimal number
    """
    return degrees + minutes / 60. + seconds / 3600.


def swap():
    """
    Changes conversion modes between "WGS84 to L-Est97" and "L-Est97 to WGS84" and displays it in GUI
    :return:
    """
    v = unit1.get()
    unit1.set(unit2.get())
    unit2.set(v)
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry1.insert(0, answer1.get())
    entry2.insert(0, answer2.get())
    answer1.__del__()
    answer2.__del__()


root = Tk()
root.title("Python Advanced HW1")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
xInput = StringVar()
yInput = StringVar()
answer2 = StringVar()
answer1 = StringVar()
unit1 = StringVar()
unit2 = StringVar()
unit1.set("WGS84")
unit2.set("Est97")
entry1 = ttk.Entry(mainframe, width=17, textvariable=xInput)
entry1.grid(column=1, row=1, sticky=(W, E))
entry2 = ttk.Entry(mainframe, width=17, textvariable=yInput)
entry2.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=answer2).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Convert", command=calculate).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="Swap", command=swap).grid(column=4, row=3, sticky=W)
ttk.Label(mainframe, text="in").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, textvariable=answer1).grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="in").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, textvariable=unit1).grid(column=4, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=unit2).grid(column=4, row=2, sticky=(W, E))
entry1.insert(0,"59°23'43.02"+'"')
entry2.insert(0,"24°39'50.78"+'"')
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
entry1.focus()
root.bind('<Return>', calculate)
root.mainloop()

