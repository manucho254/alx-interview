#!/usr/bin/python3
""" Log parsing module
"""
import sys

status_codes = {}
possible_codes = [200, 301, 400, 401, 403, 404, 405, 500]
line_count = 0
total_size = 0
status_code = 0


def print_status(codes, total):
    """print status codes
    Args:
        codes: status codes dict
        total: total size
    """
    print("File size: {}".format(total))
    for key, val in sorted(codes.items()):
        print("{}: {}".format(key, val))


try:
    for line in sys.stdin:
        split_line = line.split(" ")
        line_count += 1

        try:
            status_code = int(split_line[-2])
            total_size += int(split_line[-1])
        except Exception as e:
            continue

        if status_code in possible_codes:
            if status_codes.get(status_code):
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

        if line_count % 10 == 0 and line_count >= 10:
            print_status(status_codes, total_size)

except KeyboardInterrupt:
    print_status(status_codes, total_size)
    sys.exit(0)
