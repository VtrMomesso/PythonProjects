"""
Copyrights 2024 - By Victor dos Santos - BYU-I

    This is a test program that test the water_flow.py file.
    There are three functions that will be verified as the
    following:

    # water_column_height

    # pressure_gain_from_water_height

    # pressure_loss_from_pipe 
"""

# Import the necessaries files to work this project
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe
from pytest import approx
import pytest
import math


def test_water_column_height():
    """Verify that the water_column_height function works correctly.

    Parameters: 
        tower_height, tank_height
    Return: nothing
    """

    column_height = water_column_height(0.0, 0.0)
    assert column_height == approx(0.0)

    column_height = water_column_height(0.0, 10.0)
    assert column_height == approx(7.5)

    column_height = water_column_height(25.0, 0.0)
    assert column_height == approx(25.0)

    column_height = water_column_height(48.3, 12.8)
    assert column_height == approx(57.9)


def test_pressure_gain_from_water_height():

    assert pressure_gain_from_water_height(0) == approx(0.00)
    assert pressure_gain_from_water_height(30.2) == approx(295.628)
    assert pressure_gain_from_water_height(50.0) == approx(489.450)


def test_pressure_loss_from_pipe():

    tolerance = 0.001

    if abs(-61.576) < tolerance:

        assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx(0.00, abs=tolerance)
        assert pressure_loss_from_pipe(0.048692, 200.00, 0.00, 1.75) == approx(0.00, abs=tolerance)
        assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx(0.00, abs=tolerance)
        assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=tolerance)
        assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs= tolerance)
        assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, abs=tolerance)
        assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=tolerance)


pytest.main(["-v", "--tb=line", "-rN", __file__])