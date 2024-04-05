"""


Author: 
    Inspyre Softworks

Project:
    InspyredMemos

File: 
    inspyred_memo_server/utils/helpers/system/__init__.py
 

Description:
    This module imports the appropriate operating system implementation of the `open_in_file_explorer` function based on
    the operating system.
"""
import os


OS = os.name


if OS == 'nt':
    from inspyred_memo_server.utils.helpers.system.windows import *
elif OS == 'posix':
    if os.uname().sysname == 'Darwin':
        from inspyred_memo_server.utils.helpers.system.mac_os import *
    else:
        from inspyred_memo_server.utils.helpers.system.linux import *
"""
Linux, macOS, and Windows implementations of the `open_in_file_explorer` function are imported based on the operating 
system.
"""
