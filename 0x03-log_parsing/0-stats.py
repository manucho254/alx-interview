#!/usr/bin/python3
""" Log parsing module
"""
import sys


status_codes = {}
possible_codes = [200, 301, 400, 401, 403, 404, 405, 500]
line_count = 0
total_size = 0


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
        status_code = 0
        file_size = 0

        try:
            status_code = int(split_line[-2])
            file_size = int(split_line[-1])
        except Exception as e:
            pass

        if status_code in possible_codes:
            if status_codes.get(status_code) is not None:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

        if line_count % 10 == 0 and line_count >= 10:
            print_status(status_codes, total_size)

        total_size += file_size
        line_count += 1

except KeyboardInterrupt as e:
    print_status(status_codes, total_size)
    raise e
