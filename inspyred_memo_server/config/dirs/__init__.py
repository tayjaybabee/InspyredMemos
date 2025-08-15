"""


Author: 
    Inspyre Softworks

Project:
    InspyredMemos

File: 
    inspyred_memo_server/dirs/__init__.py
 

Description:
    

"""
from inspyred_memo_server.config.dirs.defaults import DEFAULT_DIRS
from pathlib import Path
import json
from inspyred_memo_server.utils.decorators import property_alias, validate_type


@property_alias('data', 'data_dir')
@property_alias('cache', 'cache_dir')
@property_alias('config', 'config_dir')
@property_alias('log', 'log_dir')
class AppDirs:
    """
    Manages the directories for the InspyredMemos application.

    Attempts to determine directories from initialization parameters and a cache file,
    falling back to default directories if necessary.
    """

    def __init__(self, data_dir=None, config_dir=None, log_dir=None):
        """
        Initializes the application directories.

        Args:
            data_dir (Path, optional): The initial data directory.
            config_dir (Path, optional): The initial config directory.
            log_dir (Path, optional): The initial log directory.
        """
        self.__data_dir = None
        self.__cache_dir = None
        self.__config_dir = None
        self.__log_dir = None

        self._initialized = False

        self.data_dir = data_dir or self._load_dir_from_cache('data')
        self.cache_dir = None
        self.config_dir = config_dir or self._load_dir_from_cache('config')
        self.log_dir = log_dir or self._load_dir_from_cache('log')

        self.__directories = [
            self.data_dir,
            self.cache_dir,
            self.config_dir,
            self.log_dir,
        ]

        self._ensure_dirs_exist()
        self._initialized = True
        self._update_cache_if_needed()

    @property
    def data_dir(self):
        return self.__data_dir

    @data_dir.setter
    @validate_type(str, Path, type(None))
    def data_dir(self, new):
        self.__data_dir = self._resolve_dir('data', new, DEFAULT_DIRS.data)
        if self._initialized:
            self._update_cache_if_needed()

    @property
    def cache_dir(self):
        return self.__cache_dir

    @cache_dir.setter
    @validate_type(str, Path, type(None))
    def cache_dir(self, new):
        self.__cache_dir = self._resolve_dir('cache', new, DEFAULT_DIRS.cache)
        if self._initialized:
            self._update_cache_if_needed()

    @property
    def config_dir(self):
        return self.__config_dir

    @config_dir.setter
    @validate_type(str, Path, type(None))
    def config_dir(self, new):
        self.__config_dir = self._resolve_dir('config', new, DEFAULT_DIRS.config)
        if self._initialized:
            self._update_cache_if_needed()

    @property
    def initialized(self):
        return self._initialized

    @property
    def log_dir(self):
        return self.__log_dir

    @log_dir.setter
    @validate_type(str, Path, type(None))
    def log_dir(self, new):
        self.__log_dir = self._resolve_dir('log', new, DEFAULT_DIRS.log)
        if self._initialized:
            self._update_cache_if_needed()

    def _ensure_dirs_exist(self):
        """
        Ensures that all directories exist, creating them if necessary.
        """
        for dir_path in self.__directories:
            dir_path.mkdir(parents=True, exist_ok=True)

    def _update_cache(self):
        """
        Updates the cache file with the current directory paths.
        """
        cache_file_path = DEFAULT_DIRS.cache / 'app_dirs.cache'
        
        # Ensure the cache directory exists
        cache_file_path.parent.mkdir(parents=True, exist_ok=True)
        
        cache = {
            'data': str(self.data_dir),
            'config': str(self.config_dir),
            'log': str(self.log_dir)
        }

        try:
            with open(cache_file_path, 'w') as cache_file:
                json.dump(cache, cache_file)
        except IOError as e:
            print(f"Error writing directory cache: {e}")

    def _update_cache_if_needed(self):
        """
        Updates the cache file if the directories have changed.
        """
        cache_file_path = DEFAULT_DIRS.cache / 'app_dirs.cache'
        if cache_file_path.exists():
            try:
                with open(cache_file_path, 'r') as cache_file:
                    cache = json.load(cache_file)
                    if cache.get('data') != str(self.data_dir) or \
                            cache.get('config') != str(self.config_dir) or \
                            cache.get('log') != str(self.log_dir):
                        self._update_cache()
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error reading directory cache: {e}")
        else:
            self._update_cache()

    def _load_dir_from_cache(self, dir_type):
        """
        Loads a directory path from the cache file.

        Args:
            dir_type (str): The type of directory to load ('data', 'config', 'log').

        Returns:
            Path or None: The loaded directory path, or None if not found or invalid.
        """
        cache_file_path = DEFAULT_DIRS.cache / 'app_dirs.cache'
        if cache_file_path.exists():
            try:
                with open(cache_file_path, 'r') as cache_file:
                    cache = json.load(cache_file)
                    dir_path = cache.get(dir_type)
                    if dir_path and str(dir_path) != 'None':
                        try:
                            return Path(dir_path).expanduser().resolve()
                        except Exception:
                            return None
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error reading directory cache: {e}")

        return None

    def _resolve_dir(self, name, new, default):
        """Normalize a str|Path|None into a resolved Path."""
        if new is None:
            new = default
        if not isinstance(new, (str, Path)):
            raise TypeError(f"{name} directory must be str or Path, got {type(new)}")
        return Path(new).expanduser().resolve()


APP_DIRS = AppDirs()
