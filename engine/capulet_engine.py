from engine.engine import Engine

class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        print(f"Current mileage: {self.current_mileage}, Last service mileage: {self.last_service_mileage}")
        return self.current_mileage - self.last_service_mileage > 30000
