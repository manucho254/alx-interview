#!/usr/bin/python3
""" Log parsing module
"""
import sys

if __name__ == "__main__":
    while True:
        try:
            status_codes = {
                200: 0,
                301: 0,
                400: 0,
                401: 0,
                403: 0,
                404: 0,
                405: 0,
                500: 0,
            }
            line_count = 0
            total_size = 0

            for line in sys.stdin:
                split_line = line.split(" ")
                status_code: str = split_line[-2]
                file_size = split_line[-1]

                if line_count % 10 == 0 and line_count >= 10:
                    print("File size: {}".format(total_size))

                if status_code.isnumeric() and line_count >= 10:
                    code = int(status_code)
                    status_codes[code] += 1
                    print("{}: {}".format(status_code, status_codes.get(code)))

                total_size += int(file_size)
                line_count += 1

        except KeyboardInterrupt as e:
            raise e
