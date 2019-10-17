from abc import ABC, abstractmethod
import inspect
import time

import smbus
import sys

"""
* Below is also a good one to have, but be careful i2cdump from the below cause the sht31 interface to become unstable for me
 * and requires a hard-reset to recover correctly.
 * sudo apt-get install i2c-tools
 *
 * on PI make sure below 2 commands are in /boot/config.txt
 * dtparam=i2c_arm=on
 * dtparam=i2c1_baudrate=10000
 * I know we are slowing down the baurate from optimal, but it seems to be the most stable setting in my testing.
 * add another 0 to the above baudrate for max setting, ie dtparam=i2c1_baudrate=100000
"""

import struct

from pi_ager_cx_exception import *

class cl_i2c_bus_logic():
    
    __error_counter = 0
    __measuring_intervall = 300
    

    def __init__(self, o_sensor_type):
        self.o_sensor_type = o_sensor_type
        bus1 = smbus.SMBus(1)
    def get_i2c_bus(self):
        return bus1

class th_i2c_bus_logic():
    
    def __init__(self):
        pass
    
class cl_fact_i2c_bus_logic(ABC):
    __o_instance = None
        
    @classmethod
    def set_instance(self, i_instance):
        """
        Factory method to set the i2c logic instance
        """
        logger.debug(pi_ager_logging.me())
        cl_fact_i2c_bus_logic.__o_instance = i_instance
        
    @classmethod        
    def get_instance(self):
        """
        Factory method to get the i2c logic instance
        """
        logger.debug(pi_ager_logging.me())
        if cl_fact_i2c_bus_logic.__o_instance is not None:
            return(cl_fact_i2c_bus_logic.__o_instance)
        cl_fact_i2c_bus_logic.__o_instance = cl_i2c_bus_logic()
        return(cl_fact_i2c_bus_logic.__o_instance)

    def __init__(self):
        """
        Constructor i2c logic factory
        """
        logger.debug(pi_ager_logging.me())
        pass    
    
    def __init__(self):
        pass    