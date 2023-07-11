#!/usr/bin/python3
"""
This script adds all command line arguments to a Python list and saves them
to a file named add_item.json using JSON representation.
"""

from sys import argv
from os import path
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if path.exists(filename):
    try:
        items = load_from_json_file(filename)
    except json.JSONDecodeError:
        items = []
else:
    items = []

for arg in argv[1:]:
    items.append(arg)

save_to_json_file(items, filename)
