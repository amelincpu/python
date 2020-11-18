import re

match_re = (r'Protocol (?P<port>\S+) (?P<ip>(?:\d+\.){3}\d+) mac (?P<mac>(?:\w+\.){2}\w+)')

print('\n', '*'*50, '\n',  end='')
with open('C:/Users/Alex/Dropbox/Phyton/regular_expressions/log.txt') as log_file:
    for file_line in log_file:
        match = re.search(match_re, file_line)
        print(match.group(1, 2, 3))

print('\n', '*'*50, '\n',  end='')
with open('C:/Users/Alex/Dropbox/Phyton/regular_expressions/log.txt') as log_file:
    log_buffer = log_file.read()
search_result = [match2.groups() for match2 in re.finditer(match_re, log_buffer)] # 'finditer' returns all non-overlapping matches

print(search_result)
