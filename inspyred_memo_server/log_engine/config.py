"""


Author: 
    Inspyre Softworks

Project:
    InspyredMemos

File: 
    inspyred_memo_server/log_engine/config.py
 

Description:
    Configuration for the log engine.

"""
from inspyred_memo_server.config.dirs import APP_DIRS
from pathlib import Path


class LogConfig:
    """
    Configuration for the logging engine.
    
    Attributes:
        log_dir (Path): The directory where log files are stored.
        log_level (str): The logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    """
    
    def __init__(self, log_dir=None, log_level='INFO'):
        """
        Initialize the log configuration.
        
        Args:
            log_dir (Path, optional): The directory for log files. Defaults to APP_DIRS.log_dir.
            log_level (str, optional): The logging level. Defaults to 'INFO'.
        """
        self.log_dir = log_dir if log_dir is not None else APP_DIRS.log_dir
        self.log_level = log_level
        
    @property
    def log_file_path(self):
        """Get the path to the main log file."""
        return self.log_dir / 'inspyred_memos.log'

