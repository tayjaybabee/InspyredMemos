"""


Author: 
    Inspyre Softworks

Project:
    InspyredMemos

File: 
    inspyred_memo_server/config/__init__.py
 

Description:
    

"""
from inspyred_memo_server.config.dirs import DEFAULT_DIRS

__all__ = ['DATABASE_URL']

# The database URL.
DATABASE_URL = f'sqlite:///{DEFAULT_DIRS.data}/memos.db'
