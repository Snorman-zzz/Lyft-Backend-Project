from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, sensors_readings):
        self.sensors_readings = sensors_readings

    def needs_service(self):
        return sum(self.sensors_readings) >= 3