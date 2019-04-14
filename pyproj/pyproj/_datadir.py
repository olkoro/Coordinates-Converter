# encoding: utf-8
# module pyproj._datadir
# from /Users/olkoro/Desktop/PythonCourse/test/venv/lib/python3.7/site-packages/pyproj/_datadir.cpython-37m-darwin.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import os as os # /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/os.py

# functions

def cstrencode(pystr): # reliably restored by inspect
    """ encode a string into bytes.  If already bytes, do nothing. """
    pass

def get_data_dir(): # reliably restored by inspect
    """
    The order of preference for the data directory is:
    
        1. The one set by pyproj.datadir.set_data_dir (if exists & valid)
        2. The internal proj directory (if exists & valid)
        3. The directory in PROJ_LIB (if exists & valid)
        4. The directory on the PATH (if exists & valid)
    
        Returns
        -------
        str: The valid data directory.
    """
    pass

def pystrdecode(cstr): # reliably restored by inspect
    """ Decode a string to a python string. """
    pass

# classes

class ProjError(RuntimeError):
    """ Raised when a Proj error occurs. """
    def __init__(self, error_message): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    internal_proj_error = None


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x10f913a90>'

__pyx_capi__ = {
    'get_pyproj_context': None, # (!) real value is '<capsule object "PJ_CONTEXT *(void)" at 0x10f668ae0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pyproj._datadir', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x10f913a90>, origin='/Users/olkoro/Desktop/PythonCourse/test/venv/lib/python3.7/site-packages/pyproj/_datadir.cpython-37m-darwin.so')"

__test__ = {}

