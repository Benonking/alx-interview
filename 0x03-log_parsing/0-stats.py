#!/usr/bin/python3

"""
Log parsing
"""

import sys

if __name__ == '__main__':

    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(filesize))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise

# import re
# import sys
# from collections import defaultdict

# if __name__ == "__main__":
#     # Regular expression pattern for the input format
#     input_pattern = re.compile(r'^\S+ - \[.+\] "GET .+ (\d{3}) (\d+)$')

#     def main():
#         total_file_size = 0
#         status_codes = defaultdict(int)
#         line_count = 0

#         try:
#             for line in sys.stdin:
#                 line = line.strip()
#                 match = input_pattern.match(line)
#                 if not match:
#                     continue

#                 status_code, file_size = match.groups()
#                 status_code = int(status_code)
#                 file_size = int(file_size)

#                 total_file_size += file_size
#                 status_codes[status_code] += 1

#                 line_count += 1

#                 if line_count % 10 == 0:
#                     print("Total file size:", total_file_size)
#                     for code in sorted(status_codes):
#                         if code in [200, 301, 400, 401, 403, 404, 405, 500]:
#                             print(f"{code}: {status_codes[code]}")

#         except KeyboardInterrupt:
#             print("Total file size:", total_file_size)
#             for code in sorted(status_codes):
#                 if code in [200, 301, 400, 401, 403, 404, 405, 500]:
#                     print(f"{code}: {status_codes[code]}")
