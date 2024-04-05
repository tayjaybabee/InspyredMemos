"""


Author: 
    Inspyre Softworks

Project:
    InspyredMemos

File: 
    inspyred_memo_server/user/__init__.py
 

Description:
    

"""
import bcrypt
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Set up base class for declarative base
Base = declarative_base()


class User(Base):
    """
    User class for storing user data.

    Attributes:
        id (int):
            The user ID.

        username (str):
            The username.

        password (str):
            The hashed password.
    """
    __tablename__ = 'users'
    __id = Column(Integer, primary_key=True)

    __username = Column(String, unique=True, nullable=False)
    __hashed_pass = Column(Text, nullable=False)

    @property
    def hashed_password(self):
        """
        Gets the hashed password.

        Returns:
            Column[Text]:
                The hashed password.
        """
        return self.__hashed_pass

    @property
    def id(self):
        """
        Gets the user ID.

        Returns:
            Column[Integer]:
                The user ID.
        """
        return self.__id

    @property
    def username(self):
        """
        Gets the username.

        Returns:
            Column[String]:
                The username.
        """
        return self.__username

    def set_password(self, password: str):
        """
        Sets the password for the user.

        Parameters:
            password (str):
                The password to set.

        Returns:
            None
        """
        self.__hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.hashed_password.encode('utf-8'))
