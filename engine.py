from datetime import date

class Engine():
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        return 'bool'


class CapuletEngine(Engine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return 'bool'


class WilloughbyEngine(Engine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return 'bool'


class SternmanEngine(Engine):
    def __init__(self, last_service_date, warning_light_on):
        super().__init__(last_service_date)
        self.warning_light_on = warning_light_on

    def needs_service(self):
        return 'bool'







