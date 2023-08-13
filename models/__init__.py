#!/usr/bin/python3
""" Import modules and packages for our AirBnB project """

from models.engine import file_storage
storage = file_storage.FileStorage()

storage.reload()
