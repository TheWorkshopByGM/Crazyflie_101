import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

# URI to the Crazyflie to connect to
uri = 'radio://0/80/2M/E7E7E7E7E7'

def simple_connect():

    print("Yeah, I'm connected! :D")
    time.sleep(3)
    print("Now I will disconnect!")

if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()
    print("Hello world!")
    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        print("I'm in!")
        simple_connect()