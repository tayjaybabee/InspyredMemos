"""


Author: 
    Inspyre Softworks

Project:
    InspyredMemos

File: 
    inspyred_memo_server/database/crypt/__init__.py
 

Description:
    

"""
import keyring
from cryptography.fernet import Fernet
from inspyred_memo_server.__about__ import __PROG__ as PROG_NAME
from inspyred_memo_server.errors.database import EncryptionKeyNotFoundError


class EncryptionKey:
    """
    Manages the encryption key using the system keyring for secure storage.

    Attributes:
        keyring_service (str):
            The name of the keyring service used to store the encryption key.

        keyring_user (str):
            The keyring user under which the encryption key is stored.
    """

    def __init__(self, keyring_service: str = PROG_NAME, keyring_user: str = 'default'):
        """
        Initializes the encryption key manager.

        Args:
            keyring_service (str):
                The name of the keyring service used to store the encryption key.

            keyring_user (str):
                The keyring user under which the encryption key is stored.
        """
        self.__keyring_service = keyring_service
        self.__keyring_user = keyring_user

    @property
    def keyring_service(self):
        """
        Gets the keyring service name.

        Returns:
            str:
                The keyring service name.
        """
        return self.__keyring_service

    @property
    def keyring_user(self):
        """
        Gets the keyring user name.

        Returns:
            str:
                The keyring user name.
        """
        return self.__keyring_user

    def generate_key(self) -> bytes:
        """
        Generates a new encryption key and stores it in the system keyring.

        Returns:
            bytes:
                The generated encryption key.
        """
        # Generate a new key
        key = Fernet.generate_key()

        # Store the key
        self.store_key(key)

        # Return the key to caller.
        return key

    def store_key(self, key: bytes):
        """
        Stores the encryption key in the system keyring.

        Args:
            key (bytes):
                The encryption key to store.
        """
        keyring.set_password(self.keyring_service, self.keyring_user, key.decode())

    def _retrieve_key(self):
        """
        Retrieves the encryption key from the system keyring.

        Returns:
            bytes:
                The encryption key.

        Raises:
            EncryptionKeyNotFoundError:
                If the encryption key is not found in the system keyring.
        """
        key = keyring.get_password(self.keyring_service, self.keyring_user)
        if not key:
            raise EncryptionKeyNotFoundError('Encryption key not found in system keyring.')

        return key.encode()

    def get_key(self):
        """
        Gets the encryption key from the system keyring.

        Returns:
            bytes:
                The encryption key.
        """
        try:
            return self._retrieve_key()
        except EncryptionKeyNotFoundError:
            return self.generate_key()


def generate_cipher():
    """
    Generates a new cipher for encryption and decryption.

    Returns:
        Fernet:
            The Fernet cipher.
    """
    key_manager = EncryptionKey()
    key = key_manager.get_key()
    return Fernet(key)


class EncryptionManager:
    """
    Handles the encryption and decryption of database fields using Fernet encryption.
    """

    def __init__(self, key):
        self.fernet_key = key
        self.cipher_suite = Fernet(self.fernet_key)

    def encrypt(self, data):
        """
        Encrypts data using the Fernet cipher.
        """
        return self.cipher_suite.encrypt(data.encode('utf-8')).decode('utf-8')

    def decrypt(self, data):
        return self.cipher_suite.decrypt(data.encode('utf-8')).decode('utf-8')


KEY_MAN = EncryptionKey()
KEY = KEY_MAN.get_key()
ENCRYPT_MAN = EncryptionManager(KEY)
