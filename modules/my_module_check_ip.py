"""
Checking IP address module
"""

import ipaddress


def f_check_ip(v_ip):
    '''
    the function checks an ip is correct
    '''
    try:
        ipaddress.ip_address(v_ip)
        return True
    except ValueError:
        return False