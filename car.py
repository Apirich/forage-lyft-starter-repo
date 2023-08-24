from serviceable import Serviceable

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class Car(Serviceable):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        pass


class CalliopeCar(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(current_date, last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        battery = SpindlerBattery(self.current_date, self.last_service_date)
        return 'boolEngine or boolBattery'


class GlissadeCar(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(current_date, last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        battery = SpindlerBattery(self.current_date, self.last_service_date)
        return 'boolEngine or boolBattery'


class PalindromeCar(Car):
    def __init__(self, current_date, last_service_date, warning_light_on):
        super().__init__(current_date, last_service_date)
        self.warning_light_on = warning_light_on

    def needs_service(self):
        engine = SternmanEngine(self.warning_light_on)
        battery = SpindlerBattery(self.current_date, self.last_service_date)
        return 'boolEngine or boolBattery'


class RorschachCar(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(current_date, last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        battery = NubbinBattery(self.current_date, self.last_service_date)
        return 'boolEngine or boolBattery'



class ThovexCar(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(current_date, last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        battery = NubbinBattery(self.current_date, self.last_service_date)
        return 'boolEngine or boolBattery'

