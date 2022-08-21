# AUTOGENERATED! DO NOT EDIT! File to edit: ..\nbs\00_core.ipynb.

# %% auto 0
__all__ = ['get_joiner_url', 'get_base_url']

# %% ..\nbs\00_core.ipynb 1
from IPython.display import display, Markdown
from random import randint

# %% ..\nbs\00_core.ipynb 7
def get_joiner_url(roomname, username, password):
    # new users use this link
    return f'https://vdo.ninja/?room={roomname}&password={password}&broadcast&l={username}&m&ad&sl&view'

def get_base_url(roomname, password):
    # director initiates room with this link
    return f'https://vdo.ninja/?director={roomname}&password={password}'
