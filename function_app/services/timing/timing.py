# code imports
from os import getenv
from pytz import timezone
from datetime import datetime


# functions
def get_time() -> dict:
    '''function to load the configs used by the endpoints

    returns
    -------
    output : dict
        a dictionary containing the value of time in datetime and string
    '''
    zone = getenv('TIME_ZONE') 
    tz = timezone(zone)
    time_now = datetime.now(tz)
    time_now_str = time_now.strftime('%d-%m-%Y %H:%M:%S')
    output = {'string': time_now_str, 
              'datetime': time_now,
              'time_zone': zone.replace('/', '-')}
    return output