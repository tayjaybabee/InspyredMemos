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
from inspyred_memo_server.utils.decorators import property_alias


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

        self.__initialized = False

        self._set_directory('data', data_dir or self._normalize_cached('data'), DEFAULT_DIRS.data)
        self._set_directory('cache', None, DEFAULT_DIRS.cache)
        self._set_directory('config', config_dir or self._normalize_cached('config'), DEFAULT_DIRS.config)
        self._set_directory('log', log_dir or self._normalize_cached('log'), DEFAULT_DIRS.log)

        self.__directories = [
            self.data_dir,
            self.cache_dir,
            self.config_dir,
            self.log_dir,
        ]

        self._ensure_dirs_exist()
        self.__initialized = True
        self._update_cache_if_needed()

    @property
    def data_dir(self):
        return self.__data_dir

    @data_dir.setter
    def data_dir(self, new):
        self._set_directory('data', new, DEFAULT_DIRS.data)

    @property
    def cache_dir(self):
        return self.__cache_dir

    @cache_dir.setter
    def cache_dir(self, new):
        self._set_directory('cache', new, DEFAULT_DIRS.cache)

    @property
    def config_dir(self):
        return self.__config_dir

    @config_dir.setter
    def config_dir(self, new):
        self._set_directory('config', new, DEFAULT_DIRS.config)

    def initialized(self):
        return self.__initialized

    @property
    def log_dir(self):
        return self.__log_dir

    @log_dir.setter
    def log_dir(self, new):
        self._set_directory('log', new, DEFAULT_DIRS.log)

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
            Path or None: The loaded directory path, or None if not found.
        """
        cache_file_path = DEFAULT_DIRS.cache / 'app_dirs.cache'
        if cache_file_path.exists():
            try:
                with open(cache_file_path, 'r') as cache_file:
                    cache = json.load(cache_file)
                    dir_path = cache.get(dir_type)
                    if dir_path:
                        return Path(dir_path)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error reading directory cache: {e}")

        return None

    def _normalize_cached(self, dir_type):
        """Return a cached Path or None if missing."""
        raw = self._load_dir_from_cache(dir_type)
        if raw is None:
            return None
        return Path(raw)

    def _set_directory(self, name, new_dir, default_dir):
        """
        Sets a directory attribute with validation and cache update.
        
        Args:
            name (str): The directory type (data, cache, config, log).
            new_dir (Path | str | None): The new directory path.
            default_dir (Path): The default directory path to use if new_dir is None.
        """
        if new_dir is None:
            new_dir = default_dir
        
        # Validate and convert to Path
        if isinstance(new_dir, str):
            new_dir = Path(new_dir)
        elif not isinstance(new_dir, Path):
            raise TypeError(f"{name} must be str or Path, got {type(new_dir)}")

        final = new_dir.expanduser().resolve()
        super().__setattr__(f"_{self.__class__.__name__}__{name}_dir", final)

        if getattr(self, f"_{self.__class__.__name__}__initialized", False):
            self._update_cache_if_needed()


APP_DIRS = AppDirs()
