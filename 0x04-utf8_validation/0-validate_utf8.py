#!/usr/bin/python3
'''
Module 0-Validate_utf8
Define function validateUTF8 - checks if a dataset id utf-8 valid or  not
'''


def validUTF8(data):
    '''
    '''
    continuation_bytes = 0
    for byte in data:
        # Check the 8 least significant bits of the byte
        byte = byte & 0xFF

        # If we're expecting continuation bytes
        if continuation_bytes > 0:
            # Check if the two most significant bits of the byte are '10'
            if (byte >> 6) == 0b10:
                continuation_bytes -= 1
            else:
                return False
        else:
            # Determine the number of continuation
            # bytes for the current character
            if (byte >> 7) == 0b0:
                # 1-byte character (0xxxxxxx)
                continuation_bytes = 0
            elif (byte >> 5) == 0b110:
                # 2-byte character (110xxxxx)
                continuation_bytes = 1
            elif (byte >> 4) == 0b1110:
                # 3-byte character (1110xxxx)
                continuation_bytes = 2
            elif (byte >> 3) == 0b11110:
                # 4-byte character (11110xxx)
                continuation_bytes = 3
            else:
                return False

    # If there are remaining expected continuation
    # bytes, it's an invalid sequence
    return continuation_bytes == 0
