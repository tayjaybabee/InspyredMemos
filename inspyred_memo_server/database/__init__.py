"""


Author: 
    Inspyre Softworks

Project:
    InspyredMemos

File: 
    inspyred_memo_server/database/__init__.py
 

Description:
    

"""
from sqlalchemy import event, create_engine
from sqlalchemy.orm import sessionmaker
from inspyred_memo_server.config import DATABASE_URL
from inspyred_memo_server.database.crypt import ENCRYPT_MAN
from inspyred_memo_server.database.user import User, Base


@event.listens_for(User, 'before_insert')
def encrypt_password(mapper, connection, target):
    """
    Encrypts the password before inserting a user.
    """
    target.hashed_password = ENCRYPT_MAN.encrypt(target.hashed_password)


@event.listens_for(User, 'before_update')
def encrypt_password(mapper, connection, target):
    """
    Encrypts the password before updating a user.
    """
    target.hashed_password = ENCRYPT_MAN.encrypt(target.hashed_password)


@event.listens_for(User, 'load')
def decrypt_password(target, context):
    """
    Decrypts the password after loading a user.
    """
    target.hashed_password = ENCRYPT_MAN.decrypt(target.hashed_password)


DB_ENGINE = create_engine(DATABASE_URL)
Session = sessionmaker(bind=DB_ENGINE)
DB_SESSION = Session()
Base.metadata.create_all(DB_ENGINE)
