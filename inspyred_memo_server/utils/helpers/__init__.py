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
        _win_open_in_file_explorer(path)
    elif os.name == 'posix':
        if os.uname().sysname == 'Darwin':
            _mac_open_in_file_explorer(path)
        else:
            _linux_open_in_file_explorer(path)
    else:
        raise OSError('Unsupported operating system.')
