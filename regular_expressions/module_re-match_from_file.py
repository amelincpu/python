import re

match_re = (r'Protocol (?P<port>\S+) (?P<ip>(?:\d+\.){3}\d+) mac (?P<mac>(?:\w+\.){2}\w+)')

with open('C:/Users/Alex/Dropbox/Phyton/regular_expressions/log.txt') as log_file:
    for file_line in log_file:
        match = re.search(match_re, file_line)
        print(match.group(1, 2, 3))