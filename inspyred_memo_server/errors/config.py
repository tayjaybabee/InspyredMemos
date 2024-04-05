"""


Author: 
    Inspyre Softworks

Project:
    InspyredMemos

File: 
    inspyred_memo_server/errors/config.py
 

Description:
    

"""
from inspyred_memo_server.errors import InspyredMemoServerError


__all__ = [
    'ConfigNotLoadedError',
    'ConfigFileNotLoadedError',
    'ConfigFileNotFoundError',
]


class ConfigError(InspyredMemoServerError):
    """
    Base class for configuration errors.
    """
    __base_message = 'Configuration Error: A configuration error has occurred!'

    def __init__(self, message=None):
        """
        Initialize the ConfigError class.

        Parameters:
            message (str):
                The message to display when the error is raised.
        """
        if message is None:
            message = self.__base_message

        super(ConfigError, self).__init__(message)


class ConfigNotLoadedError(ConfigError):
    """
    Error raised when the configuration has not been loaded, but an operation requires/expects it to be.
    """

    __base_message = 'Configuration Not Loaded: The configuration has not been loaded! Try loading it first. '\
                     '(Use the load() method.)'

    def __init__(self, message=__base_message):
        """
        Initialize the ConfigNotLoadedError class.

        Parameters:
            message (str):
                The message to display when the error is raised.
        """
        super(ConfigNotLoadedError, self).__init__(message)


class ConfigFileError(ConfigError):
    __base_message = 'Configuration File Error: An error occurred while processing the configuration file!'

    def __init__(self, message=__base_message):
        super(ConfigFileError, self).__init__(message)


class ConfigFileNotLoadedError(ConfigFileError):
    __base_message = 'Configuration File Not Loaded: The configuration file has not been loaded!'

    def __init__(self, message=__base_message):
        super(ConfigFileNotLoadedError, self).__init__(message)


class ConfigFileNotFoundError(ConfigFileError, FileNotFoundError):
    __base_message = 'Configuration File Not Found: The configuration file was not found!'

    def __init__(self, message=__base_message):
        super(ConfigFileNotFoundError, self).__init__(message)
