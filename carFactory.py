from car import CalliopeCar, GlissadeCar, PalindromeCar, RorschachCar, ThovexCar

def CarFactory():
    calliope = CalliopeCar(current_date, last_service_date, current_mileage, last_service_mileage)
    glissade = GlissadeCar(current_date, last_service_date, current_mileage, last_service_mileage)
    palindrome = PalindromeCar(current_date, last_service_date, warning_light_on)
    rorschach = RorschachCar(current_date, last_service_date, current_mileage, last_service_mileage)
    thovex = ThovexCar(current_date, last_service_date, current_mileage, last_service_mileage)

