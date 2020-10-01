'''
Domino
'''

import time

v_a = -1
v_b = 0

for v_number in range(7):
    v_a = v_a + 1
    for v_number2 in range(v_a, 7):
        v_b = v_b + 1
        print('domino {: >2} = {} : {}'.format(v_b, v_number, v_number2))
        time.sleep(0.2)