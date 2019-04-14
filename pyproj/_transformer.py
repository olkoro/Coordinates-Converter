# encoding: utf-8
# module pyproj._transformer
# from /Users/olkoro/Desktop/PythonCourse/test/venv/lib/python3.7/site-packages/pyproj/_transformer.cpython-37m-darwin.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import math as math # /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload/math.cpython-37m-darwin.so
import pyproj._crs as __pyproj__crs
import pyproj._proj as __pyproj__proj


# Variables with simple values

_DOUBLESIZE = 8

# functions

def cstrencode(pystr): # reliably restored by inspect
    """ encode a string into bytes.  If already bytes, do nothing. """
    pass

def pystrdecode(cstr): # reliably restored by inspect
    """ Decode a string to a python string. """
    pass

# classes

class CRS(__pyproj__crs._CRS):
    """
    A pythonic Coordinate Reference System manager.
    
        The functionality is based on other fantastic projects:
    
        * https://github.com/opendatacube/datacube-core/blob/83bae20d2a2469a6417097168fd4ede37fd2abe5/datacube/utils/geometry/_base.py
        * https://github.com/mapbox/rasterio/blob/c13f0943b95c0eaa36ff3f620bd91107aa67b381/rasterio/_crs.pyx
    """
    @classmethod
    def from_epsg(cls, *args, **kwargs): # real signature unknown
        """
        Make a CRS from an EPSG code
        
                Parameters
                ----------
                code : int or str
                    An EPSG code. Strings will be converted to integers.
        
                Notes
                -----
                The input code is not validated against an EPSG database.
        
                Returns
                -------
                ~CRS
        """
        pass

    @classmethod
    def from_string(cls, *args, **kwargs): # real signature unknown
        """
        Make a CRS from an EPSG, PROJ, or WKT string
        
                Parameters
                ----------
                proj_string : str
                    An EPSG, PROJ, or WKT string.
        
                Returns
                -------
                ~CRS
        """
        pass

    @classmethod
    def from_user_input(cls, *args, **kwargs): # real signature unknown
        """
        Make a CRS from various input
        
                Dispatches to from_epsg, from_proj, or from_string
        
                Parameters
                ----------
                value : obj
                    A Python int, dict, or str.
        
                Returns
                -------
                ~CRS
        """
        pass

    def get_geod(self): # reliably restored by inspect
        """
        Returns
                -------
                ~pyproj.geod.Geod: Geod object based on the ellipsoid.
        """
        pass

    def __init__(self, projparams=None, **kwargs): # reliably restored by inspect
        """
        Initialize a CRS class instance with a WKT string,
                a proj,4 string, a proj.4 dictionary, or with
                proj.4 keyword arguments.
        
                CRS projection control parameters must either be given in a
                dictionary 'projparams' or as keyword arguments. See the proj.4
                documentation (https://github.com/OSGeo/proj.4/wiki) for more information
                about specifying projection parameters.
        
                Example usage:
        
                >>> from pyproj import CRS
                >>> crs_utm = CRS.from_user_input(26915)
                >>> crs_utm
                <CRS: epsg:26915>
                Name: NAD83 / UTM zone 15N
                Ellipsoid:
                - semi_major_metre: 6378137.00
                - semi_minor_metre: 6356752.31
                - inverse_flattening: 298.26
                Area of Use:
                - name: North America - 96°W to 90°W and NAD83 by country
                - bounds: (-96.0, 25.61, -90.0, 84.0)
                Prime Meridian:
                - longitude: 0.0000
                - unit_name: degree
                - unit_conversion_factor: 0.01745329
                Axis Info:
                - Easting[E] (east) EPSG:9001 (metre)
                - Northing[N] (north) EPSG:9001 (metre)
                <BLANKLINE>
                >>> crs_utm.area_of_use.bounds
                (-96.0, 25.61, -90.0, 84.0)
                >>> crs_utm.ellipsoid.inverse_flattening
                298.257222101
                >>> crs_utm.ellipsoid.semi_major_metre
                6378137.0
                >>> crs_utm.ellipsoid.semi_minor_metre
                6356752.314140356
                >>> crs_utm.prime_meridian.unit_name
                'degree'
                >>> crs_utm.prime_meridian.unit_conversion_factor
                0.017453292519943295
                >>> crs_utm.prime_meridian.longitude
                0.0
                >>> crs = CRS(proj='utm', zone=10, ellps='WGS84')
                >>> crs.to_proj4()
                '+proj=utm +zone=10 +ellps=WGS84 +units=m +no_defs +type=crs'
                >>> crs.to_wkt()
                'PROJCRS["unknown",BASEGEOGCRS["unknown",DATUM["Unknown based on WGS84 ellipsoid",ELLIPSOID["WGS 84",6378137,298.257223563,LENGTHUNIT["metre",1],ID["EPSG",7030]]],PRIMEM["Greenwich",0,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8901]]],CONVERSION["UTM zone 10N",METHOD["Transverse Mercator",ID["EPSG",9807]],PARAMETER["Latitude of natural origin",0,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8801]],PARAMETER["Longitude of natural origin",-123,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8802]],PARAMETER["Scale factor at natural origin",0.9996,SCALEUNIT["unity",1],ID["EPSG",8805]],PARAMETER["False easting",500000,LENGTHUNIT["metre",1],ID["EPSG",8806]],PARAMETER["False northing",0,LENGTHUNIT["metre",1],ID["EPSG",8807]],ID["EPSG",16010]],CS[Cartesian,2],AXIS["(E)",east,ORDER[1],LENGTHUNIT["metre",1,ID["EPSG",9001]]],AXIS["(N)",north,ORDER[2],LENGTHUNIT["metre",1,ID["EPSG",9001]]]]'
                >>> geod = crs.get_geod()
                >>> "+a={:.0f} +f={:.8f}".format(geod.a, geod.f)
                '+a=6378137 +f=0.00335281'
                >>> crs.is_projected
                True
                >>> crs.is_geographic
                False
                >>> crs.is_valid
                True
        """
        pass

    def __reduce__(self): # reliably restored by inspect
        """ special method that allows CRS instance to be pickled """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pyproj.crs', '__doc__': '\\n    A pythonic Coordinate Reference System manager.\\n\\n    The functionality is based on other fantastic projects:\\n\\n    * https://github.com/opendatacube/datacube-core/blob/83bae20d2a2469a6417097168fd4ede37fd2abe5/datacube/utils/geometry/_base.py\\n    * https://github.com/mapbox/rasterio/blob/c13f0943b95c0eaa36ff3f620bd91107aa67b381/rasterio/_crs.pyx\\n\\n    ', '__init__': <function CRS.__init__ at 0x101199158>, 'from_epsg': <classmethod object at 0x100f71278>, 'from_string': <classmethod object at 0x100f712b0>, 'from_user_input': <classmethod object at 0x100f71320>, 'get_geod': <function CRS.get_geod at 0x101199840>, '__reduce__': <function CRS.__reduce__ at 0x1011998c8>, '__str__': <function CRS.__str__ at 0x101199950>, '__repr__': <function CRS.__repr__ at 0x1011999d8>, '__dict__': <attribute '__dict__' of 'CRS' objects>, '__weakref__': <attribute '__weakref__' of 'CRS' objects>})"


class Proj(__pyproj__proj.Proj):
    """
    performs cartographic transformations (converts from
        longitude,latitude to native map projection x,y coordinates and
        vice versa) using proj (https://github.com/OSGeo/proj.4/wiki).
    
        A Proj class instance is initialized with proj map projection
        control parameter key/value pairs. The key/value pairs can
        either be passed in a dictionary, or as keyword arguments,
        or as a proj4 string (compatible with the proj command). See
        http://www.remotesensing.org/geotiff/proj_list for examples of
        key/value pairs defining different map projections.
    
        Calling a Proj class instance with the arguments lon, lat will
        convert lon/lat (in degrees) to x/y native map projection
        coordinates (in meters).  If optional keyword 'inverse' is True
        (default is False), the inverse transformation from x/y to
        lon/lat is performed. If optional keyword 'errcheck' is True (default is
        False) an exception is raised if the transformation is invalid.
        If errcheck=False and the transformation is invalid, no
        exception is raised and 1.e30 is returned. If the optional keyword
        'preserve_units' is True, the units in map projection coordinates
        are not forced to be meters.
    
        Works with numpy and regular python array objects, python
        sequences and scalars.
    """
    def definition_string(self): # reliably restored by inspect
        """
        Returns formal definition string for projection
        
                >>> Proj('+init=epsg:4326').definition_string()
                'proj=longlat datum=WGS84 no_defs ellps=WGS84 towgs84=0,0,0'
                >>>
        """
        pass

    def is_geocent(self): # reliably restored by inspect
        """
        Returns
                -------
                bool: True if projection in geocentric (x/y) coordinates
        """
        pass

    def is_latlong(self): # reliably restored by inspect
        """
        Returns
                -------
                bool: True if projection in geographic (lon/lat) coordinates.
        """
        pass

    def to_latlong(self): # reliably restored by inspect
        """
        return a new Proj instance which is the geographic (lat/lon)
                coordinate version of the current projection
        """
        pass

    def to_latlong_def(self): # reliably restored by inspect
        """
        return the definition string of the geographic (lat/lon)
                coordinate version of the current projection
        """
        pass

    def __call__(self, *args, **kw): # reliably restored by inspect
        """
        Calling a Proj class instance with the arguments lon, lat will
                convert lon/lat (in degrees) to x/y native map projection
                coordinates (in meters).  If optional keyword 'inverse' is True
                (default is False), the inverse transformation from x/y to
                lon/lat is performed. If optional keyword 'errcheck' is True (default is
                False) an exception is raised if the transformation is invalid.
                If errcheck=False and the transformation is invalid, no
                exception is raised and 1.e30 is returned.
        
                Inputs should be doubles (they will be cast to doubles if they
                are not, causing a slight performance hit).
        
                Works with numpy and regular python array objects, python
                sequences and scalars, but is fastest for array objects.
        """
        pass

    def __init__(self, projparams=None, preserve_units=True, **kwargs): # reliably restored by inspect
        """
        initialize a Proj class instance.
        
                See the proj documentation (https://github.com/OSGeo/proj.4/wiki)
                for more information about projection parameters.
        
                Parameters
                ----------
                projparams: int, str, dict, pyproj.CRS
                    A proj.4 or WKT string, proj.4 dict, EPSG integer, or a pyproj.CRS instnace.
                preserve_units: bool
                    If false, will ensure +units=m.
                **kwargs:
                    proj.4 projection parameters.
        
        
                Example usage:
        
                >>> from pyproj import Proj
                >>> p = Proj(proj='utm',zone=10,ellps='WGS84', preserve_units=False) # use kwargs
                >>> x,y = p(-120.108, 34.36116666)
                >>> 'x=%9.3f y=%11.3f' % (x,y)
                'x=765975.641 y=3805993.134'
                >>> 'lon=%8.3f lat=%5.3f' % p(x,y,inverse=True)
                'lon=-120.108 lat=34.361'
                >>> # do 3 cities at a time in a tuple (Fresno, LA, SF)
                >>> lons = (-119.72,-118.40,-122.38)
                >>> lats = (36.77, 33.93, 37.62 )
                >>> x,y = p(lons, lats)
                >>> 'x: %9.3f %9.3f %9.3f' % x
                'x: 792763.863 925321.537 554714.301'
                >>> 'y: %9.3f %9.3f %9.3f' % y
                'y: 4074377.617 3763936.941 4163835.303'
                >>> lons, lats = p(x, y, inverse=True) # inverse transform
                >>> 'lons: %8.3f %8.3f %8.3f' % lons
                'lons: -119.720 -118.400 -122.380'
                >>> 'lats: %8.3f %8.3f %8.3f' % lats
                'lats:   36.770   33.930   37.620'
                >>> p2 = Proj('+proj=utm +zone=10 +ellps=WGS84', preserve_units=False) # use proj4 string
                >>> x,y = p2(-120.108, 34.36116666)
                >>> 'x=%9.3f y=%11.3f' % (x,y)
                'x=765975.641 y=3805993.134'
                >>> p = Proj(init="epsg:32667", preserve_units=False)
                >>> 'x=%12.3f y=%12.3f (meters)' % p(-114.057222, 51.045)
                'x=-1783506.250 y= 6193827.033 (meters)'
                >>> p = Proj("+init=epsg:32667")
                >>> 'x=%12.3f y=%12.3f (feet)' % p(-114.057222, 51.045)
                'x=-5851386.754 y=20320914.191 (feet)'
                >>> # test data with radian inputs
                >>> p1 = Proj(init="epsg:4214")
                >>> x1, y1 = p1(116.366, 39.867)
                >>> '{:.3f} {:.3f}'.format(x1, y1)
                '2.031 0.696'
                >>> x2, y2 = p1(x1, y1, inverse=True)
                >>> '{:.3f} {:.3f}'.format(x2, y2)
                '116.366 39.867'
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pyproj.proj\', \'__doc__\': "\\n    performs cartographic transformations (converts from\\n    longitude,latitude to native map projection x,y coordinates and\\n    vice versa) using proj (https://github.com/OSGeo/proj.4/wiki).\\n\\n    A Proj class instance is initialized with proj map projection\\n    control parameter key/value pairs. The key/value pairs can\\n    either be passed in a dictionary, or as keyword arguments,\\n    or as a proj4 string (compatible with the proj command). See\\n    http://www.remotesensing.org/geotiff/proj_list for examples of\\n    key/value pairs defining different map projections.\\n\\n    Calling a Proj class instance with the arguments lon, lat will\\n    convert lon/lat (in degrees) to x/y native map projection\\n    coordinates (in meters).  If optional keyword \'inverse\' is True\\n    (default is False), the inverse transformation from x/y to\\n    lon/lat is performed. If optional keyword \'errcheck\' is True (default is\\n    False) an exception is raised if the transformation is invalid.\\n    If errcheck=False and the transformation is invalid, no\\n    exception is raised and 1.e30 is returned. If the optional keyword\\n    \'preserve_units\' is True, the units in map projection coordinates\\n    are not forced to be meters.\\n\\n    Works with numpy and regular python array objects, python\\n    sequences and scalars.\\n    ", \'__init__\': <function Proj.__init__ at 0x1010a76a8>, \'__call__\': <function Proj.__call__ at 0x101199a60>, \'is_latlong\': <function Proj.is_latlong at 0x101199ae8>, \'is_geocent\': <function Proj.is_geocent at 0x101199b70>, \'definition_string\': <function Proj.definition_string at 0x101199bf8>, \'to_latlong_def\': <function Proj.to_latlong_def at 0x101199c80>, \'to_latlong\': <function Proj.to_latlong at 0x101199d08>, \'__dict__\': <attribute \'__dict__\' of \'Proj\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Proj\' objects>})'


class ProjError(RuntimeError):
    """ Raised when a Proj error occurs. """
    def __init__(self, error_message): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    internal_proj_error = None


class _Transformer(object):
    # no doc
    def from_pipeline(self, *args, **kwargs): # real signature unknown
        pass

    def from_proj(self, *args, **kwargs): # real signature unknown
        pass

    def set_radians_io(self, *args, **kwargs): # real signature unknown
        pass

    def _init_crs_to_crs(self, *args, **kwargs): # real signature unknown
        pass

    def _transform(self, *args, **kwargs): # real signature unknown
        pass

    def _transform_sequence(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    input_geographic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    input_radians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_pipeline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    output_geographic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    output_radians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    projections_equivalent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    projections_exact_same = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skip_equivalent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x1011a9b38>'

__spec__ = None # (!) real value is "ModuleSpec(name='pyproj._transformer', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x1011a9b38>, origin='/Users/olkoro/Desktop/PythonCourse/test/venv/lib/python3.7/site-packages/pyproj/_transformer.cpython-37m-darwin.so')"

__test__ = {}

