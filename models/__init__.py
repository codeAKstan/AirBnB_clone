#!/usr/bin/python3
""" the __init_ file, makes a package """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
