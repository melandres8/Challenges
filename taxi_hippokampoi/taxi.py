import random
import string

"""
    Taxi class for hippokampoi
"""


class Taxi:
    def __init__(self, typo="", driver_name="", cy_capacity=""):
        self.__typo = typo
        self.__driver_name = driver_name
        self.__cy_capacity = cy_capacity

    @classmethod
    def generate_plates(cls):
        plate = []
        plate_letters = string.ascii_uppercase
        for item in range(73):
            num = str(random.randint(100, 999))
            plate.append(num)
        plates_t = tuple(plate)
        return ''.join(random.choice(plate_letters) for letter in range(3)) + ' ' + num

    @property
    def get_driver(self):
        return self.__driver_name

    @get_driver.setter
    def set_driver(self, name):
        self.__driver_name = name

    @property
    def get_typo(self):
        return self.__typo

    @get_typo.setter
    def set_typo(self, taxi_type):
        self.__typo = taxi_type

    @property
    def get_cylinder(self):
        return self.__cy_capacity

    @get_cylinder.setter
    def set_cylinder(self, cylinder):
        self.__cy_capacity = cylinder
