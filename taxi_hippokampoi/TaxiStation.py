"""
    Taxi Station class for hippokampoi
"""


class TaxiStation:
    def __init__(self, nro_taxis=0, staff=""):
        self.__nro_taxis = nro_taxis
        self.__staff = staff

    @property
    def get_nro_taxis(self):
        return self.__nro_taxis

    @get_nro_taxis.setter
    def set_nro_taxis(self, taxis):
        self.__nro_taxis = taxis

    @property
    def get_staff(self):
        return self.__staff

    @get_nro_taxis.setter
    def set_staff(self, staff_role):
        self.__staff = staff_role
