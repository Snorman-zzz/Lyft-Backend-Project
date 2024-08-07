import unittest

from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        sensors_readings = [0.8, 0.8, 0.8, 0.8]
        tires = OctoprimeTires(sensors_readings)

        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        sensors_readings = [0.5, 0.5, 0.5, 0.5]
        tires = OctoprimeTires(sensors_readings)

        self.assertFalse(tires.needs_service())