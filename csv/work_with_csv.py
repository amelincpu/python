import os
import sys
import csv

print('\n', '*'*50, '\n', end='')

with open(os.path.join(sys.path[0], 'ap_list.csv')) as csv_file:
    print(type(csv_file))
    print(csv_file)
    for file_line in csv_file:
        print(file_line, end='')
print('\n', '*'*50, '\n', end='')

with open(os.path.join(sys.path[0], 'ap_list.csv')) as csv_file:
    csvreader = csv.reader(csv_file)
    print(list(csvreader))
print('\n', '*'*50, '\n', end='')

with open(os.path.join(sys.path[0], 'ap_list.csv')) as csv_file:
    csvreader = csv.reader(csv_file)
    print(type(csvreader))
    for readerline in csvreader:
        print(readerline)
print('\n', '*'*50, '\n', end='')

with open(os.path.join(sys.path[0], 'ap_list.csv')) as csv_file:
    csvreader = csv.DictReader(csv_file)
    print(type(csvreader))
    for readerline in csvreader:
        print(readerline, '\n')
        print(readerline['AP Name'], 'SN:', readerline['Serial'], '\n')
print('\n', '*'*50, '\n', end='')

data_for_csv = [['device', 'hostname', 'ip', 'location'],
                ['switch', 'sw1', '1.1.1.3', 'floor1'],
                ['router', 'rt1', '1.3.1.1', 'floor2'],
                ['switch', 'sw2', '1.1.1.1', 'floor2'],
                ['switch', 'sw3', '1.1.2.1', 'floor3']]
with open(os.path.join(sys.path[0], 'device_list.csv'), 'w', newline='') as new_csv_file:
    write_csv = csv.writer(new_csv_file, quoting=csv.QUOTE_ALL)
    for data_line in data_for_csv:
        write_csv.writerow(data_line)
with open(os.path.join(sys.path[0], 'device_list.csv')) as csv_file:
    print(type(csv_file))
    print(csv_file)
    for file_line in csv_file:
        print(file_line, end='')
print('\n', '*'*50, '\n', end='')