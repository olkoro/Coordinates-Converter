# encoding: utf-8
# module pyproj._proj
# from /Users/olkoro/Desktop/PythonCourse/test/venv/lib/python3.7/site-packages/pyproj/_proj.cpython-37m-darwin.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import math as math # /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload/math.cpython-37m-darwin.so

# Variables with simple values

proj_version_str = '6.0.0'

_DOUBLESIZE = 8

# functions

def cstrencode(pystr): # reliably restored by inspect
    """ encode a string into bytes.  If already bytes, do nothing. """
    pass

def pystrdecode(cstr): # reliably restored by inspect
    """ Decode a string to a python string. """
    pass

# classes

class Proj(object):
    # no doc
    def is_exact_same(self, *args, **kwargs): # real signature unknown
        """ Compares projections to see if they are exactly the same. """
        pass

    def _fwd(self, *args, **kwargs): # real signature unknown
        """
        forward transformation - lons,lats to x,y (done in place).
                if errcheck=True, an exception is raised if the forward transformation is invalid.
                if errcheck=False and the forward transformation is invalid, no exception is
                raised and 1.e30 is returned.
        """
        pass

    def _inv(self, *args, **kwargs): # real signature unknown
        """
        inverse transformation - x,y to lons,lats (done in place).
                if errcheck=True, an exception is raised if the inverse transformation is invalid.
                if errcheck=False and the inverse transformation is invalid, no exception is
                raised and 1.e30 is returned.
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Compares projections to see if they are equivalent. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ special method that allows pyproj.Proj instance to be pickled """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    definition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_inverse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if this projection has an inverse"""

    proj_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class ProjError(RuntimeError):
    """ Raised when a Proj error occurs. """
    def __init__(self, error_message): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    internal_proj_error = None


class TransProj(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x1080fe390>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyproj._proj', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x1080fe390>, origin='/Users/olkoro/Desktop/PythonCourse/test/venv/lib/python3.7/site-packages/pyproj/_proj.cpython-37m-darwin.so')"

__test__ = {}

