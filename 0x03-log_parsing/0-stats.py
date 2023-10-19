#!/usr/bin/python3
'''
Read stdin line by line and compute metrics
'''

import sys
import re
from collections import defaultdict


def get_status_code(line):
    '''extract status code'''
    match = re.match(r'"GET .+ (\d{3})', line)
    if match:
        return int(match.group(1))
    return None


def main():
    file_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.match(r'^S+ - \[.+] "GET ." \d{3} \d+$', line)
            if not match:
                continue
            file_size += int(line.split()[-1])
            status_code = get_status_code(line)

            if status_code is not None:
                status_codes[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print("Total file size: File size:", file_size)
            for code in sorted(status_codes):
                print(f"{code}: {status_codes[code]}")

    except KeyboardInterrupt:
        print("Total file size: File size:", file_size)
        for code in sorted(status_codes):
            print(f"{code}: {status_codes[code]}")
