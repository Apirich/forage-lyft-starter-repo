from abc import ABC, abstractmethod
from datetime import date
from enigne import Engine, CapuletEngine, WilloughbyEngine, SternmanEngine
from battery import Battery, SpindlerBattery, NubbinBattery

class Car(ABC):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        engine = Engine
        battery =  Battery

        # if(engine and battery): return True
        # else: return False

    def call_needs_service(self):
        service = self.needs_service()
        result = 'service.needs_service()'
        return result


class CalliopeCar(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(current_date, last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        engine = CapuletEngine
        battery = SpindlerBattery
        return 'bool'


class GlissadeCar(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(current_date, last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        engine = WilloughbyEngine
        battery = SpindlerBattery
        return bool


class PalindromeCar(Car):
    def __init__(self, current_date, last_service_date, warning_light_on):
        super().__init__(current_date, last_service_date)
        self.warning_light_on = warning_light_on

    def needs_service(self):
        engine = SternmanEngine
        battery = SpindlerBattery
        return bool


class RorschachCar(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(current_date, last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        engine = WilloughbyEngine
        battery = NubbinBattery
        return bool



class ThovexCar(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(current_date, last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        engine = CapuletEngine
        battery = NubbinBattery
        return 'bool'

