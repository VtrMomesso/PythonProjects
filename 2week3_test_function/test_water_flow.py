
from water_flow import water_column_height, pressure_gain_from_water_height 
from pytest import approx
import pytest

def test_water_column_height():
    column_height = water_column_height(0.0, 0.0)
    assert column_height == approx(0.0)

    column_height = water_column_height(0.0, 10.0)
    assert column_height == approx(7.5)

    column_height = water_column_height(25.0, 0.0)
    assert column_height == approx(25.0)

    column_height = water_column_height(48.3, 12.8)
    assert column_height == approx(57.9)


def test_pressure_gain_from_water_height():

    assert pressure_gain_from_water_height(0) == approx(0.001)
    assert pressure_gain_from_water_height(0) == approx(0.001)
    assert pressure_gain_from_water_height(0) == approx(0.001)
    

pytest.main(["-v", "--tb=line", "-rN", __file__])