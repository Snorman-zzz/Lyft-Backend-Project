from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, sensors_readings):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(sensors_readings)
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, sensors_readings):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoprimeTires(sensors_readings)
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_palindrome(current_mileage, last_service_mileage, warning_light_is_on, sensor_readings):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_mileage, last_service_mileage)
        tires = CarriganTires(sensor_readings)
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, sensors_readings):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(sensors_readings)
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_Thovex(current_date, last_service_date, current_mileage, last_service_mileage, sensors_readings):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTires(sensors_readings)
        return Car(engine, battery, tires)