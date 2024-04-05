from configparser import ConfigParser
from pathlib import Path
from inspyred_memo_server.config.dirs import APP_DIRS
from inspyred_memo_server.utils.decorators import validate_type
from inspyred_memo_server.errors.config import *

from inspy_logger import InspyLogger


DEFAULT_CONFIG = {
    'DEFAULT' : {
        'smtp_server': 'smtp.email.com',
        'smtp_port': '587',
        'smtp_user': 'user',
        'smtp_password': 'password',
    }
}


class EMailConfig:
    """
    Class to hold email configuration settings.

    Parameters:
        config_file (str, Path):
               The path to the configuration file.

    Attributes:
        smtp_server (str):
            The SMTP server to use.

        smtp_port (str):
            The port to use for the SMTP server.

        smtp_user (str):
            The username to use for the SMTP server.

        smtp_password (str):
            The password to use for the SMTP server.
    """
    DEFAULTS = DEFAULT_CONFIG['DEFAULT']

    def __init__(
            self,
            config_file=APP_DIRS.config_dir.joinpath('email.ini'),
            auto_create=False,
            auto_load=False,
            no_write=False,
            server=DEFAULT_CONFIG['smtp_server'],
            port=DEFAULT_CONFIG['smtp_port'],
            user=DEFAULT_CONFIG['smtp_user'],
            password=DEFAULT_CONFIG['smtp_password']
    ):
        self.__auto_load = None
        self.__auto_create = None
        self.__config_file = None
        self.__config = None
        self.__no_write = None

        self.config_file = config_file



        self.auto_create = auto_create

        self.auto_load = auto_load

        self.config_file = config_file

    def _ensure_user_section(self):
        if not self.config and self.auto_load:
            self.load_config()
        elif not self.config and not self.auto_load:
            raise ConfigNotLoadedError()

        if not self.config.has_section('USER'):
            self.config.add_section('USER')

    @property
    def auto_create(self):
        return self.__auto_create

    @auto_create.setter
    @validate_type(bool)
    def auto_create(self, new):
        self.__auto_create = new

    @property
    def auto_load(self):
        return self.__auto_load

    @auto_load.setter
    @validate_type(bool)
    def auto_load(self, new):
        self.__auto_load = new
        if new:
            self.load_config()

    @property
    def config(self):
        return self.__config

    @property
    def config_file(self):
        """
        The path to the configuration file.
        """
        return self.__config_file

    @config_file.setter
    @validate_type(str, Path, preferred_type=Path)
    def config_file(self, new):
        self.__config_file = new

        if self.config_file.exists():
            if self.auto_load:
                self.load_config()
        else:
            if self.auto_create:
                self.create_config()

    @property
    def no_write(self):
        """
        Whether to write to the configuration file.
        """
        return self.__no_write

    @no_write.setter
    @validate_type(bool)
    def no_write(self, new):
        """
        Whether to write to the configuration file.
        """
        self.__no_write = new

    @property
    def server(self):
        """
        The SMTP server to use.
        """
        return self.config.get(
            'USER',
            'smtp_server',
            fallback=self.DEFAULTS['smtp_server']
        )

    @server.setter
    @validate_type(str)
    def server(self, new):
        """
        The SMTP server to use.
        """
        self._ensure_user_section()

        self.config.set(
            'USER',
            'smtp_server',
            new
        )

    @property
    def user(self):
        """
        The username to use for the SMTP server.
        """
        return self.config.get(
            'USER',
            'smtp_user',
            fallback=self.DEFAULTS['smtp_user']
        )


    def create_config(self):
        if not self.config_file.parent.exists():
            self.config_file.parent.mkdir(parents=True)

        self.config.read_dict(DEFAULT_CONFIG)

        self.config['DEFAULT']['smtp_server'] = self.__server
        self.config['DEFAULT']['smtp_port'] = self.__port
        self.config['DEFAULT']['smtp_user'] = self.__user
        self.config['DEFAULT']['smtp_password'] = self.__password

        self.save_config()


    def load_config(self):
        self.__config = ConfigParser()
        if self.config_file.exists():
            self.config.read(self.config_file)

    def save_config(self):
        if not self.no_write:

        with self.config_file.open('w') as f:
            self.config.write(f)
