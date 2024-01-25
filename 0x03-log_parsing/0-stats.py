#!/usr/bin/python3
""" Log parsing module
"""
import sys


def print_status(status_codes, total_size):
    """print status codes"""
    print("File size: {}".format(total_size))
    for key, val in status_codes.items():
        print("{}: {}".format(key, val))


status_codes = {}
possible_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
line_count = 0
total_size = 0


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            split_line = line.split(" ")
            status_code: str = split_line[-2]
            file_size = split_line[-1]

            if status_code.isnumeric() and status_code in possible_codes:
                if status_codes.get(status_code) is not None:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

            if line_count % 10 == 0 and line_count >= 10:
                print_status(status_codes, total_size)

            total_size += int(file_size)
            line_count += 1

    except KeyboardInterrupt as e:
        print_status(status_codes, total_size)
        raise e
