from getpass import getpass
from tqdm import tqdm
from time import sleep
import random

"""
    main file of hippokampoi
"""
Person = __import__('person').Person
Taxi = __import__('taxi').Taxi
TaxiStation = __import__('TaxiStation').TaxiStation

"""Important"""
list_typo = []
typeof = ["Normal", "Trunk"]
for item in range(73):
    rand_typo = random.choice(typeof)
    list_typo.append(rand_typo)

"""Cylinder capacity"""
cylinder = Taxi()
list_c = []
list_cy = ["1.200", "1.500", "2.000", "1.600", "1.800"]
for cy in range(len(list_cy)):
    rand_cy = random.choice(list_cy)
cylinder.set_cylinder = rand_cy

"""Staff login"""
station1 = TaxiStation()
staff = Person()
staff.set_name = str(input("""If you are here, it's because
you're a staff member.
Please, enter your name: """))
station1.set_staff = staff.set_name
staff.set_role = "Staff"
password = getpass("password: ")

"""
    below here I'm handling the service.
    Integrate options:
    1. Delivery request
    2. Request more taxis
    3. Sending message
"""
plate = Taxi.generate_plates()
if password == "staff1234":
    print("{:s} member: {:s} has joined!".format(staff.get_role, station1.get_staff))
    print("""
        ====================================
        Please, select an option below here:
        -> (1) Enter a taxi member.
        -> (2) Request for a small cab.
        -> (3) Request for a trunk cab.
        -> (4) Check number of taxis.
        -> (5) Exit.
        ====================================
    """)
    while 1:
        petition = int(input("Please, select one option: "))
        if petition == 1:
            """Creating objects"""
            new_person = Person()
            taxi_type = Taxi()
            station1 = TaxiStation()

            """Taxi driver object"""
            new_person.set_name = str(input("Taxi driver name: "))
            taxi_type.set_driver = new_person.set_name
            print("--> Role >> Taxi driver.")
            print("--> Name: {}".format(taxi_type.get_driver))
            print("--> Plates: {}".format(plate))
            print("--> Cylinder: {}".format(cylinder.get_cylinder))

            """Costumer object"""
        if petition == 2:
            new_person.set_name = str(input(" Costumer name: "))
            taxi_type.set_typo = "Normal"
            if taxi_type.set_typo == "Normal":
                print("Assigning service...")
                for item in tqdm(range(100)):
                    sleep(0.02)
                list_typo.remove("Normal")
                print("********* Assigned service! *********")
                print("Taxi driver assigned is >> {:s}".format(taxi_type.get_driver))
                print("--> Type: {}".format(taxi_type.get_typo))
                print("--> Plates: {}".format(plate))
            print("--> Role >> Costumer.")
            print("--> Name: {}".format(new_person.get_name))
        if petition == 3:
            new_person.set_name = str(input(" Costumer name: "))
            taxi_type.set_typo = "Trunk"
            if taxi_type.set_typo == "Trunk":
                print("Assigning service...")
                for item in tqdm(range(100)):
                    sleep(0.02)
                list_typo.remove("Trunk")
                print("********* Assigned service! *********")
                print("Taxi driver assigned is >> {:s}".format(taxi_type.get_driver))
                print("--> Type: {}".format(taxi_type.get_typo))
                print("--> Plates: {}".format(plate))
            print("--> Role >> Costumer.")
            print("--> Name: {}".format(new_person.get_name))

            """Taxi Station"""
        if petition == 4:
            station1.set_nro_taxis = len(list_typo)
            print("Available taxis: {:d}".format(station1.get_nro_taxis))
        if petition == 5:
            print("Closing program...")
            for item in tqdm(range(100)):
                sleep(0.04)
            exit(0)

else:
    print("Invalid password, try again!")
