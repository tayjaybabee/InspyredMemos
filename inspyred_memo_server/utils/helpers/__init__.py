"""


Author: 
    Inspyre Softworks

Project:
    InspyredMemos

File: 
    inspyred_memo_server/utils/helpers.py
 

Description:
    

"""
import subprocess
import os
from typing import Union
from pathlib import Path


def open_in_file_explorer(path: Union[str, Path]):
    """
    Opens the specified path in the file explorer.

    Parameters:
        path (str):
            The path to open.
    """
    if os.name == 'nt':
        from inspyred_memo_server.utils.helpers.system.windows import open_in_file_explorer as _win_open_in_file_explorer
        _win_open_in_file_explorer(path)
    elif os.name == 'posix':
        if os.uname().sysname == 'Darwin':
            from inspyred_memo_server.utils.helpers.system.mac_os import open_in_file_explorer as _mac_open_in_file_explorer
            _mac_open_in_file_explorer(path)
        else:
            from inspyred_memo_server.utils.helpers.system.linux import open_in_file_explorer as _linux_open_in_file_explorer
            _linux_open_in_file_explorer(path)
    else:
        raise OSError('Unsupported operating system.')
