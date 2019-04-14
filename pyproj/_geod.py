# encoding: utf-8
# module pyproj._geod
# from /Users/olkoro/Desktop/PythonCourse/test/venv/lib/python3.7/site-packages/pyproj/_geod.cpython-37m-darwin.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import math as math # /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload/math.cpython-37m-darwin.so

# Variables with simple values

geodesic_version_str = '1.49.3'

_DOUBLESIZE = 8

# functions

def cstrencode(pystr): # reliably restored by inspect
    """ encode a string into bytes.  If already bytes, do nothing. """
    pass

def pystrdecode(cstr): # reliably restored by inspect
    """ Decode a string to a python string. """
    pass

# classes

class Geod(object):
    # no doc
    def _fwd(self, *args, **kwargs): # real signature unknown
        """
        forward transformation - determine longitude, latitude and back azimuth
         of a terminus point given an initial point longitude and latitude, plus
         forward azimuth and distance.
         if radians=True, lons/lats are radians instead of degrees.
        """
        pass

    def _inv(self, *args, **kwargs): # real signature unknown
        """
        inverse transformation - return forward and back azimuths, plus distance
         between an initial and terminus lat/lon pair.
         if radians=True, lons/lats are radians instead of degrees.
        """
        pass

    def _npts(self, *args, **kwargs): # real signature unknown
        """ given initial and terminus lat/lon, find npts intermediate points. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ special method that allows pyproj.Geod instance to be pickled """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    es = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    initstring = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sphere = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class GeodError(RuntimeError):
    """ Raised when a Geod error occurs. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x1103c4748>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyproj._geod', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x1103c4748>, origin='/Users/olkoro/Desktop/PythonCourse/test/venv/lib/python3.7/site-packages/pyproj/_geod.cpython-37m-darwin.so')"

__test__ = {}

