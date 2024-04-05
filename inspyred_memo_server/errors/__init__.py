"""


Author: 
    Inspyre Softworks

Project:
    InspyredMemos

File: 
    inspyred_memo_server/errors/__init__.py
 

Description:
    

"""


class InspyredMemoServerError(Exception):
    __base_message = 'A general application error has occurred!'
    __info_unavailable = 'No additional information is available.'
    __additional_info_stub = 'More information from the subclass is available: '

    """
    Base exception class for the application.
    
    Attributes:
        message (str):
            Human-readable string describing the exxception.
            
        code (int):
            Error code representing the exception.
            
    Examples:
        >>> raise InspyredMemoServerError('An error has occurred!', 100)
        Traceback (most recent call last):
        ...
        InspyredMemoServerError: ('An error has occurred!', 100)
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

    @additional_info.setter
    def additional_info(self, new):
        self.__additional_info = new

    @property
    def base_message(self):
        """
        The base message for the error message.

        Returns:
            str:
                The base message for the error message.

        Examples:
            >>> raise InspyredMemoServerError('An error has occurred!', 100)
            Traceback (most recent call last):
            ...
            InspyredMemoServerError: ('An error has occurred!', 100)
        """
        return self.__base_message

    @property
    def info_unavailable(self):
        """
        A message indicating that no additional information is available.

        Returns:
            str:
                A message indicating that no additional information is available.
        """
        return self.__info_unavailable

    @property
    def code(self):
        """
        The error code for the exception.

        Returns:
            int:
                The error code for the exception.
        """
        return self.__code

    @property
    def message(self):
        """
        The full error message.

        Returns:
            str:
                The full error message.
        """
        return self.__message

    def build_message(self):
        """
        Constructs the full error message; including base and additional information.

        Returns:
            str:
                The full error message.
        """
        return f'{self.__base_message}\n\n{self.additional_info}'

    def __str__(self):
        """
        Returns the full error message as a string.

        Returns:
            str:
                Then full error message as a string.
        """
        return f'{self.__message} (Error code: {self.code})'
