from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, sensors_readings):
        self.sensors_readings = sensors_readings

    def needs_service(self):
        for i in self.sensors_readings:
            if i >= 0.9:
                return True
        return False