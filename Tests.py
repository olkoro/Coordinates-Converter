"""Testing Converter.py
When running close the GUI window to proceed with testing"""
from Converter import wgs_to_est, est_to_wgs, degrees_to_decimal, decimal_to_degrees


def testWGStoEST():
    """
    Testing conversion WGS84 -> Est97 -> WGS84, comparing result to initial input
    :return:
    """
    x = "59°23'43.02"+'"'
    y = "24°39'50.78"+'"'
    assert x, y == est_to_wgs(wgs_to_est(x, y)[0], wgs_to_est(x, y)[1])


def testESTtoWGS():
    """
    Testing conversion from Est97 to WGS84 then from WFS84 to Est97
    and comparing the result Est97 coordinates with the initial coordinates
    :return:
    """
    x = 6584335.60149003
    y = 537731.0999690604
    assert (y, x) == wgs_to_est(est_to_wgs(x, y)[1], est_to_wgs(x, y)[0])


def test3():
    """
    Testing conversion WGS84 -> Est97 -> WGS84, comparing result to initial input
    :return:
    """
    x = "49°33'44.52"+'"'
    y = "29°34'51.90"+'"'
    assert x, y == est_to_wgs(wgs_to_est(x, y)[0], wgs_to_est(x, y)[1])


def test4():
    """
    Testing conversion WGS84 -> Est97 -> WGS84, comparing result to initial input
    :return:
    """
    x = "10°40'11.52"+'"'
    y = "59°34'95.01"+'"'
    assert x, y == est_to_wgs(wgs_to_est(x, y)[0], wgs_to_est(x, y)[1])


def testToDecimal():
    assert degrees_to_decimal(49, 33, 44.52) == 49.56236666666666


def testToDegrees():
    assert decimal_to_degrees(49.56236666666666) == "49° 33' 44.52"+'"'


# starting tests
testWGStoEST()
testESTtoWGS()
test3()
test4()
testToDecimal()
testToDegrees()

print("Testing Complete")