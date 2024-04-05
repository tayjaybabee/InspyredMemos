"""


Author: 
    Inspyre Softworks

Project:
    InspyredMemos

File: 
    inspyred_memo_server/log_engine/__init__.py
 

Description:
    

"""
from inspyred_memo_server.__about__ import PROGNAME, __AUTHOR__ as AUTHOR
from inspy_logger import PROG_LOGGER




APP_ROOT_LOGGER = PROG_LOGGER

APP_ROOT_LOGGER.info(f'{PROGNAME} by {AUTHOR} started.')
