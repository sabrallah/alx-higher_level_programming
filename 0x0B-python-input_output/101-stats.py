#!/usr/bin/python3
"""
This module reads from stdin line by line and computes the total file size and
the number of lines by status code. Every 10 lines and after a keyboard
interruption (CTRL + C), it prints the statistics since the beginning. The
statistics include the total file size and the number of lines by status code
in ascending order. If a status code doesn’t appear, it doesn’t print anything
for this status code.
"""

import sys


def print_stats(total_size, status_codes):
    """
    Prints the statistics including the total file size and the number of lines
    by status code in ascending order. If a status code doesn’t appear, it
    doesn’t print anything for this status code.

    :param total_size: The total file size.
    :type total_size: int
    :param status_codes: A dictionary containing
    the number of lines by status code.
    :type status_codes: dict
    """
    print("File size: {}".format(total_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print("{}: {}".format(key, status_codes[key]))


total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
counter = 0

try:
    for line in sys.stdin:
        counter += 1
        data = line.split()
        try:
            size = data[-1]
            total_size += int(size)
            status = data[-2]
            if status in status_codes:
                status_codes[status] += 1
        except Exception:
            pass
        if counter % 10 == 0:
            print_stats(total_size, status_codes)
except KeyboardInterrupt:
    pass
finally:
    print_stats(total_size, status_codes)
