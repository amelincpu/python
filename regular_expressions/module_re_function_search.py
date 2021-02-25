import re

print('\n', '*'*50, '\n', end='')

v_line = 'Interface IP-Address OK? Method Status Protocol FastEthernet0/0 10.1.1.1 YES NVRAM up up Serial1/0 10.4.4.1 YES manual up up Serial1/1 unassigned YES unset administratively down down Serial1/2 unassigned YES unset administratively down down Serial1/3 unassigned YES unset administratively down down Loopback0 1.1.1.1 YES NVRAM up up Loopback1 11.11.11.11 YES NVRAM up up Loopback11 1.2.2.2 YES NVRAM up up Loopback12 1.3.3.3 YES NVRAM up up Loopback22 111.111.111.111 YES NVRAM up up'
print(v_line, end='')

print('\n', '*'*50, '\n', end='')

print(re.search('Loopback', v_line), end='')

print('\n', '*'*50, '\n', end='')

# 'search' function works utill the first hit
# 'r' means interpreted as it is, do not use '\' as a special symbol
v_re = re.search(r'\d+\.\d+\.\d+\.\d+', v_line)
print(v_re.group())
print(type(v_re))

print('\n', '*'*50, '\n', end='')

v_re_line = v_re.group()
print(v_re_line)
print(type(v_re_line))

print('\n', '*'*50, '\n', end='')

match = re.search(r'\d{2}(.\d){3}', v_line)
print(match.group())

print('\n', '*'*50, '\n',  end='')

match = re.search('(Fast).*(Serial)', v_line)
print(match.group(), '\n')
print(match.groups())
print(match.group(1))
print(match.group(2))
print(match.group(2, 1, 2))

print(match[2])

print('\n', '*'*50, '\n',  end='')

match = re.search('(?P<name1>Fast).*(?P<name2>Serial)', v_line)
print(match.groupdict())
print(match.group('name1'))

print('\n', '*'*50, '\n',  end='')

print('\n', '*'*50, '\n', end='')
logline = 'Interface IP-Address OK? Method Status Protocol FastEthernet0/0 10.1.1.1 YES NVRAM up up Serial1/0 10.4.4.1 YES manual up up Serial1/1 unassigned YES unset administratively down down Serial1/2 unassigned YES unset administratively down down Serial1/3 unassigned YES unset administratively down down Loopback0 1.1.1.1 YES NVRAM up up Loopback1 11.11.11.11 YES NVRAM up up Loopback11 1.2.2.2 YES NVRAM up up Loopback12 1.3.3.3 YES NVRAM up up Loopback22 111.111.111.111 YES NVRAM up up'
fromlog = re.search(r'(Protocol) (\S+) (?P<ipaddress>(?:\d+\.){3}\d)', logline) # '?:' - does not retur backets value to groups
# method 'group'
print(fromlog)
print(fromlog.group())
print(fromlog.group(0))  # '0' whole match
print(fromlog.group(1))  # '1' 1st brackets match
print(fromlog.group(2))  # '2' 2nd brackets match
print(fromlog.group(3))  # '3' 3rd brackets match
print(fromlog.group(3, 2))
print(fromlog.group('ipaddress'))
print(type(fromlog.group(1)))

print('\n', '*'*50, '\n', end='')
# method 'groups' - shows all groups
print(fromlog.groups())

print('\n', '*'*50, '\n', end='')
# 'groupdict' method - returns a dictionary
print(fromlog.groupdict())

print('\n', '*'*50, '\n', end='')
print(fromlog.string) # which string was searched
print(fromlog.re) # which re was used

print('\n', '*'*50, '\n', end='')