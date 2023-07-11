i want like this code : 
#!/usr/bin/python3
"""
Module append after method.
"""


def append_after(filename="", search_string="", new_string=""):
    '''method inserting text after search string.'''
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        y = 0
        while y < len(lines):
            if search_string in lines[y]:
                lines[y:y + 1] = [lines[y], new_string]
                y += 1
            y += 1
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
