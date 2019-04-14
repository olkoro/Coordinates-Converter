# encoding: utf-8
# module pyproj._crs
# from /Users/olkoro/Desktop/PythonCourse/test/venv/lib/python3.7/site-packages/pyproj/_crs.cpython-37m-darwin.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import pyproj.exceptions as __pyproj_exceptions


# functions

def cstrencode(pystr): # reliably restored by inspect
    """ encode a string into bytes.  If already bytes, do nothing. """
    pass

def is_wkt(*args, **kwargs): # real signature unknown
    """
    Check if the input projection string is in the Well-Known Text format.
    
        Parameters
        ----------
        proj_string: str
            The projection string.
    
        Returns
        -------
        bool: True if the string is in the Well-Known Text format
    """
    pass

def pystrdecode(cstr): # reliably restored by inspect
    """ Decode a string to a python string. """
    pass

def __pyx_unpickle_AreaOfUse(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_AxisInfo(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Ellipsoid(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PrimeMeridian(*args, **kwargs): # real signature unknown
    pass

# classes

class AreaOfUse(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    east = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    north = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    south = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    west = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x1055bea50>'


class AxisInfo(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    abbrev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unit_auth_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unit_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unit_conversion_factor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unit_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x1055be1b0>'


class CRSError(__pyproj_exceptions.ProjError):
    """ Raised when a CRS error occurs. """
    def __init__(self, error_message): # reliably restored by inspect
        # no doc
        pass


class Ellipsoid(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    ellipsoid_loaded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    inverse_flattening = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The ellipsoid inverse flattening.

        Returns
        -------
        float or None: The inverse flattening if the projection is an ellipsoid.
        """

    is_semi_minor_computed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    semi_major_metre = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The ellipsoid semi major metre.

        Returns
        -------
        float or None: The semi major metre if the projection is an ellipsoid.
        """

    semi_minor_metre = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The ellipsoid semi minor metre.

        Returns
        -------
        float or None: The semi minor metre if the projection is an ellipsoid
            and the value was com
            puted.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x1055be7e0>'


class PrimeMeridian(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    longitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unit_conversion_factor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unit_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x1055bea80>'


class _CRS(object):
    # no doc
    def is_exact_same(self, *args, **kwargs): # real signature unknown
        """ Compares projections to see if they are exactly the same. """
        pass

    def to_epsg(self, *args, **kwargs): # real signature unknown
        """
        Return the EPSG code best matching the projection.
        
                Parameters
                ----------
                min_confidence: int, optional
                    A value between 0-100 where 100 is the most confident. Default is 70.
        
                Returns
                -------
                int or None: The best matching EPSG code matching the confidence level.
        """
        pass

    def to_geodetic(self, *args, **kwargs): # real signature unknown
        """
        Returns
                -------
                pyproj.CRS: The geographic (lat/lon) CRS from the current CRS.
        """
        pass

    def to_proj4(self, *args, **kwargs): # real signature unknown
        """
        Convert the projection to a proj.4 string.
        
                Parameters
                ----------
                version: int
                    The version of the proj.4 output. Default is 4.
        
                Returns
                -------
                str: The proj.4 string.
        """
        pass

    def to_wkt(self, *args, **kwargs): # real signature unknown
        """
        Convert the projection to a WKT string.
        
                Version options:
                  - WKT2_2015
                  - WKT2_2015_SIMPLIFIED
                  - WKT2_2018
                  - WKT2_2018_SIMPLIFIED
                  - WKT1_GDAL
                  - WKT1_ESRI
        
        
                Parameters
                ----------
                version: str
                    The version of the WKT output. Default is WKT2_2018.
         
                Returns
                -------
                str: The WKT string.
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
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    area_of_use = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns
        -------
        AreaOfUse: The area of use object with associated attributes.
        """

    axis_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns
        -------
        list[AxisInfo]: The list of axis information.
        """

    datum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns
        -------
        pyproj.CRS: The datum as a CRS.
        """

    ellipsoid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns
        -------
        Ellipsoid: The ellipsoid object with associated attributes.
        """

    is_geocentric = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns
        -------
        bool: True if projection in geocentric (x/y) coordinates
        """

    is_geographic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns
        -------
        bool: True if projection in geographic (lon/lat) coordinates.
        """

    is_projected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns
        -------
        bool: True if projection is a projected type.
        """

    is_valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns
        -------
        bool: True if projection is a valid type.
        """

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prime_meridian = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns
        -------
        PrimeMeridian: The CRS prime meridian object with associated attributes.
        """

    proj_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    srs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _area_of_use = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _axis_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ellipsoid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _prime_meridian = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x10586c6d8>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyproj._crs', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x10586c6d8>, origin='/Users/olkoro/Desktop/PythonCourse/test/venv/lib/python3.7/site-packages/pyproj/_crs.cpython-37m-darwin.so')"

__test__ = {}

