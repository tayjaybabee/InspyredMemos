"""


Author: 
    Inspyre Softworks

Project:
    InspyredMemos

File: 
    inspyred_memo_server/errors/databse/__init__.py
 

Description:
    

"""
from inspyred_memo_server.errors import InspyredMemoServerError


class DatabaseError(InspyredMemoServerError):
    __base_message = 'A database error has occurred!'
    __info_unavailable = 'No additional information is available.'
    __additional_info_stub = 'More information from the subclass is available: '

    """
    Base exception class for database errors.
    
    Attributes:
        message (str):
            Human-readable string describing the exxception.
            
        code (int):
            Error code representing the exception.
            
    Examples:
        >>> raise DatabaseError('An error has occurred!', 100)
        Traceback (most recent call last):
        ...
        DatabaseError: ('An error has occurred!', 100)
    """

    def __init__(self, message=None, code=0):
        self.__additional_info = message if message is not None else self.__info_unavailable
        self.__code = code
        self.__message = self.build_message()

        # Call the base class constructor with the parameters it needs.
        super().__init__(self.__message, self.__code)

    @property
    def additional_info(self):
        return self.__additional_info


class EncryptionKeyNotFoundError(DatabaseError):
    __base_message = 'An encryption key was not found!'
    __info_unavailable = __base_message
    __additional_info_stub = 'More information from the subclass is available: '

    """
    Exception class for when an encryption key is not found.
    
    Attributes:
        message (str):
            Human-readable string describing the exxception.
            
        code (int):
            Error code representing the exception.
            
    Examples:
        >>> raise EncryptionKeyNotFoundError('An error has occurred!', 100)
        Traceback (most recent call last):
        ...
        EncryptionKeyNotFoundError: ('An error has occurred!', 100)
    """

    def __init__(self, message=None, code=0):
        self.__additional_info = message if message is not None else self.__info_unavailable
        self.__code = code
        self.__message = self.build_message()

        # Call the base class constructor with the parameters it needs.
        super().__init__(self.__message, self.__code)

    @property
    def additional_info(self):
        return self.__additional_info
