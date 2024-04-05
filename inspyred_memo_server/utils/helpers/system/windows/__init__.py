"""
Author: 
    Inspyre Softworks

Project:
    InspyredMemos

File: 
    inspyred_memo_server/utils/helpers/system/windows/__init__.py
 

Description:
    This module provides a function that opens a specified path in the file explorer on Windows.

"""
from typing import Union
from pathlib import Path
import os
import subprocess


__all__ = [
    'open_in_file_explorer'
]


def open_in_file_explorer(path: Union[str, Path]):
    """
    Opens the specified path in the file explorer on Windows.

    Parameters:
        path (str):
            The path to open.
    """
    if not isinstance(path, (str, Path)):
        raise TypeError(f'path must be a str or Path, not {type(path)}')

    path = Path(path).expanduser().resolve()

    if not path.exists():
        raise FileNotFoundError(f'No such file or directory: {path}')

    if not os.name == 'nt':
        raise OSError('This function is only available on Windows.')

    subprocess.Popen(f'explorer /select,{path}')
