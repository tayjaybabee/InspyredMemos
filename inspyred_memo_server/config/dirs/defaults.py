"""


Author: 
    Inspyre Softworks

Project:
    InspyredMemos

File: 
    inspyred_memo_server/config/dirs/defaults.py
 

Description:
    

"""
from platformdirs import user_data_path, user_config_path, user_log_path
from inspyred_memo_server.__about__ import __PROG__, __AUTHOR__
from pathlib import Path


__all__ = ['DEFAULT_DIRS']


class DefaultDirs:
    """
    Default directories for InspyredMemos.

    Properties:

        cache (Path):
            The cache directory.

        data (Path):
            The data directory.

        config (Path):
            The config directory.

        log (Path):
            The log directory.
    """

    def __init__(self):
        """
        Initializes the default directories.
        """
        self.__cache = user_data_path(__PROG__, __AUTHOR__)
        self.__data = user_data_path(__PROG__, __AUTHOR__)
        self.__config = user_config_path(__PROG__, __AUTHOR__)
        self.__log = user_log_path(__PROG__, __AUTHOR__)

    @property
    def cache(self) -> Path:
        """
        Gets the cache directory.

        Returns:
            Path:
                The cache directory.
        """
        return Path(self.__cache)

    @property
    def data(self) -> Path:
        """
        Gets the data directory.

        Returns:
            Path:
                The data directory.
        """
        return Path(self.__data)

    @property
    def config(self) -> Path:
        """
        Gets the config directory.

        Returns:
            Path:
                The config directory.
        """
        return Path(self.__config)

    @property
    def log(self) -> Path:
        """
        Gets the log directory.

        Returns:
            Path:
                The log directory.
        """
        return Path(self.__log)


DEFAULT_DIRS = DefaultDirs()
