from datetime import date
from car import Car, CalliopeCar, GlissadeCar, PalindromeCar, RorschachCar, ThovexCar

def CarFactory():
    CalliopeCar(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
    GlissadeCar(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
    PalindromeCar(current_date: date, last_service_date: date, warning_light_on: bool): Car
    RorschachCar(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
    ThovexCar(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car

