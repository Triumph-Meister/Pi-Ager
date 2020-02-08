# -*- coding: utf-8 -*-

"""This class is for alarm notification."""

__author__ = "Claus Fischer"
__copyright__ = "Copyright 2019, The Pi-Ager Project"
__credits__ = ["Claus Fischer"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Claus Fischer"
__email__ = "DerBurgermeister@pi-ager.org"
__status__ = "Production"

from abc import ABC
import inspect
import pi_ager_names
import pi_ager_gpio_config
from main.pi_ager_cl_database import cl_fact_database_config, cl_ab_database_config
import RPi.GPIO as gpio
from time import sleep

from main.pi_ager_cx_exception import *

from main.pi_ager_cl_logger import cl_fact_logger
# import pi_ager_logging

# global logger
# logger = pi_ager_logging.create_logger(__name__)
        
class cl_logic_alarm:
    def __init__(self):
        # logger.debug(pi_ager_logging.me())
        cl_fact_logger.get_instance().debug(cl_fact_logger.get_instance().me())
   
        if "get_instance" not in inspect.stack()[1][3]:
            raise cx_direct_call("Please use factory class")
      
        gpio.setmode(pi_ager_gpio_config.board_mode)
        gpio.setwarnings(False)
        gpio.setup(pi_ager_gpio_config.gpio_alarm, gpio.OUT )
        self.alarm_gpio = pi_ager_gpio_config.gpio_alarm
        """
        self.replication  = 3
        self.Sleep     = 0.5
        self.High_time = 1
        self.Low_time  = 1
        """
        
        """
        Read alarm setting from the database
        """
        
        self.db_alarm = cl_fact_db_alarm().get_instance()
        self.it_alarm = self.db_alarm.read_data_from_db()
        if self.it_alarm: 
            cl_fact_logger.get_instance().debug('user_key  = ' + str(self.it_alarm[0]['user_key']))
            cl_fact_logger.get_instance().debug('api_token = ' + str(self.it_alarm[0]['api_token']))
        
        self.user_key  = str(self.it_alarm[0]['user_key'])
        self.api_token = str(self.it_alarm[0]['api_token'])
        
        self.client = Client(self.user_key, api_token=self.api_token)
    def set_alarm_type(self,DutyCycle, Frequency, replication, Sleep):
        # logger.debug(pi_ager_logging.me())
        cl_fact_logger.get_instance().debug(cl_fact_logger.get_instance().me())
        self.DutyCycle = DutyCycle
        self.Frequency = Frequency
        self.replication  = replication
        self.Sleep     = Sleep

    def execute_alarm(self):
        # logger.debug(pi_ager_logging.me())
        cl_fact_logger.get_instance().debug(cl_fact_logger.get_instance().me())
        for x in range(0, self.replication):
           gpio.output(self.alarm_gpio, True)
           sleep(self.High_time)
           gpio.output(self.alarm_gpio, False)
           sleep(self.Low_time)

    def execute_short(self, replication):
        # logger.debug(pi_ager_logging.me())
        cl_fact_logger.get_instance().debug(cl_fact_logger.get_instance().me())
        self.replication = replication
        self.Sleep    = 0.5
        self.High_time = 0.5
        self.Low_time  = 0.5
        self.execute_alarm()
           
    def execute_middle(self, replication):
        # logger.debug(pi_ager_logging.me())
        cl_fact_logger.get_instance().debug(cl_fact_logger.get_instance().me())
        self.replication = replication
        self.Sleep    = 0.5
        self.High_time = 1
        self.Low_time  = 1
        self.execute_alarm()
        
    def execute_long(self, replication):
        # logger.debug(pi_ager_logging.me())
        cl_fact_logger.get_instance().debug(cl_fact_logger.get_instance().me())
        self.replication = replication
        self.Sleep    = 0.5
        self.High_time = 2
        self.Low_time  = 2
        self.execute_alarm()

class cl_db_alarm(cl_ab_database_config):

    def build_select_statement(self):
        cl_fact_logger.get_instance().debug(cl_fact_logger.get_instance().me())
        return('SELECT * FROM config_alarm where active = 1 ')
    
class th_logic_alarm(cl_logic_alarm):   

    
    def __init__(self):
        pass


class cl_fact_logic_alarm(ABC):
    __o_instance = None
    
    @classmethod
    def set_instance(self, i_instance):
        cl_fact_logic_alarm.__o_instance = i_instance
        
    @classmethod        
    def get_instance(self):
        if cl_fact_logic_alarm.__o_instance is not None:
            return(cl_fact_logic_alarm.__o_instance)
        cl_fact_logic_alarm.__o_instance = cl_logic_alarm()
        return(cl_fact_logic_alarm.__o_instance)

    def __init__(self):
        pass    
    
class cl_fact_db_alarm(ABC):
    __o_instance = None
    
    @classmethod
    def set_instance(self, i_instance):
        """
        Factory method to set the db alarm instance
        """        
        cl_fact_logger.get_instance().debug(cl_fact_logger.get_instance().me())
        cl_fact_db_messenger.__o_instance = i_instance
        
    @classmethod        
    def get_instance(self):
        """
        Factory method to get the db alarm instance
        """        
        cl_fact_logger.get_instance().debug(cl_fact_logger.get_instance().me())
        if cl_fact_db_alarm.__o_instance is not None:
            return(cl_fact_db_alarm.__o_instance)
        cl_fact_db_alarm.__o_instance = cl_db_alarm()
        return(cl_fact_db_alarm.__o_instance)

    def __init__(self):
        """
        Constructor logic messenger factory
        """        
        cl_fact_logger.get_instance().debug(cl_fact_logger.get_instance().me())
        pass    
