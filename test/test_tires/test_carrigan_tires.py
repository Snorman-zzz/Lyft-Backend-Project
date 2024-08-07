import unittest

from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        sensors_readings = [0.9, 0.5, 0.5, 0.5]
        tires = CarriganTires(sensors_readings)

        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        sensors_readings = [0.5, 0.5, 0.5, 0.5]
        tires = CarriganTires(sensors_readings)

        self.assertFalse(tires.needs_service())