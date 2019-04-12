from pyproj import Proj, transform, Geod
from tkinter import *
from tkinter import ttk
from collections import namedtuple

def calculate(*args):
    label()
    try:
        x = float(xInput.get())
        y = float(yInput.get())
        (y, x) = est_to_wgs(x, y)
    except:
        x = xInput.get()
        y = yInput.get()
        (y, x) = wgs_to_est(x, y)
    answer0.set(x)
    answer.set(y)
def wgs_to_est(x,y):
    xdeg = float(x.split('°')[0])
    xmin = float(x.split('°')[1].split("'")[0])
    xsek = float(x.split("'")[1].split('"')[0])
    print(xdeg, xmin, xsek)
    ydeg = float(y.split('°')[0])
    ymin = float(y.split('°')[1].split("'")[0])
    ysek = float(y.split("'")[1].split('"')[0])
    print(ydeg, ymin, ysek)

    x,y = convert_degrees_to_decimal(xdeg, xmin, xsek), convert_degrees_to_decimal(ydeg, ymin, ysek)
    print(x, y)
    p1 = Proj(init='epsg:3301', preserve_units=False)
    y,x = p1(y,x)
    #y, x = round(y, 1), round(x, 1)
    return y,x
def est_to_wgs(x,y):
    p1 = Proj(init='epsg:3301', preserve_units=False)
    (x, y) = p1(y, x, inverse=True)
    return convert_decimal_to_degrees(x), convert_decimal_to_degrees(y)

def convert_decimal_to_degrees(decimal):
    # type: (float) -> Tuple[int, int, float]
    """
    Convert decimal degrees to degree-minute-second format.

    Example:
        >>> convert_decimal_to_degrees(30.56)
        (30, 33, 36)

    Args:
        Decimal: degree in decimals
    Returns:
        Tuple of degree-minute-second.
    """
    degrees = int(decimal)
    minutes = int((decimal - degrees) * 60)
    seconds = round((decimal - degrees - minutes / 60.) * 3600, 4)
    #return degrees, minutes, seconds
    return "".join(map(str, [degrees, '° ', minutes, "' ", seconds, '"']))

def convert_degrees_to_decimal(degrees, minutes, seconds):
    # type: (int, int, float) -> float
    """
    Convert degree-minute-second format to decimal degrees.

    Example:
    >>> convert_degrees_to_decimal(10, 23, 42)
    10.395

    Returns:
         Degrees in decimal format
    """
    return degrees + minutes / 60. + seconds / 3600.

def swap():
    v = unit1.get()
    entryunit1.delete(0,'end')
    entryunit1.insert(0, unit2.get())
    entryunit2.delete(0,'end')
    entryunit2.insert(0,v)

    entry1.delete(0,'end')
    entry1.insert(0,answer0.get())
    entry2.delete(0,'end')
    entry2.insert(0,answer.get())

    answer0.__del__()
    answer.__del__()

    label()
    return
def label():
    if unit2.get() == "3301":
        ttk.Label(mainframe, text= "L-Est97").grid(column=5, row=2, sticky=(W, E))
    elif unit2.get() == "4326":
        ttk.Label(mainframe, text= "WGS84").grid(column=5, row=2, sticky=(W, E))
    else:
        ttk.Label(mainframe, text="else").grid(column=5, row=2, sticky=(W, E))
    if unit1.get() == "3301":
        ttk.Label(mainframe, text="L-Est97").grid(column=5, row=1, sticky=(W, E))
    elif unit1.get() == "4326":
        ttk.Label(mainframe, text="WGS84").grid(column=5, row=1, sticky=(W, E))
    else:
        ttk.Label(mainframe, text="Other").grid(column=5, row=1, sticky=(W, E))
    return
root = Tk()
root.title("Python Advanced HW1")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

xInput = StringVar()
yInput = StringVar()
answer = StringVar()
answer0 = StringVar()
unit1 = StringVar()
unit2 = StringVar()

entry1 = ttk.Entry(mainframe, width=7, textvariable=xInput)
entry1.grid(column=1, row=1, sticky=(W, E))
entry2 = ttk.Entry(mainframe, width=7, textvariable=yInput)
entry2.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=answer).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=1, row=3, sticky=W)

ttk.Button(mainframe, text="Swap", command=swap).grid(column=4, row=3, sticky=W)

ttk.Label(mainframe, text="in").grid(column=3, row=1, sticky=W)
entryunit1 = ttk.Entry(mainframe, width=7, textvariable=unit1)
entryunit1.grid(column=4, row=1, sticky=(W, E))
entryunit1.insert(0,"4326")

entryunit2 = ttk.Entry(mainframe, width=7, textvariable=unit2)
entryunit2.grid(column=4, row=2, sticky=(W, E))
entryunit2.insert(0,"3301")

ttk.Label(mainframe, textvariable=answer0).grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="in").grid(column=3, row=2, sticky=W)
label()

entry1.insert(0,"59°23'43.02"+'"')
entry2.insert(0,"24°39'50.78"+'"')

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

entry1.focus()
root.bind('<Return>', calculate)

root.mainloop()

