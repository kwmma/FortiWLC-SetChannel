#!/usr/bin/env python3
# CLI syntax to set AP channels
# CSV from WLC with AP ID in COL1 used as input
#
# Output to        ap-output-channel.txt
#
# Kristian Winckler - 20221004 - Version 1.0
# kristian.winckler@atea.se
#

# FortiWLC (8.6-4build-2)
# interface Dot11Radio <CSV-COL1> 1 
# channel xx
# exit
# interface Dot11Radio <CSV-COL1> 2 
# channel xx
# exit

file_input = 'ap-input.csv'
file_output1 = 'ap-output-channel.txt'

channel24 = "1"
channel5 = "44"


import csv
output1 = open(file_output1, 'w')

with open(file_input) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader)
    line_count = 0
    for row in csv_reader:
        result10 = [f'interface Dot11Radio {row[0]} 1\n']
        result11 = [f'channel {channel24}\n']
        result12 = ['exit\n']
        result13 = [f'interface Dot11Radio {row[0]} 2\n']
        result14 = [f'channel {channel5}\n']
        result15 = ['exit\n']
        output1.writelines(result10)
        output1.writelines(result11)
        output1.writelines(result12)
        output1.writelines(result13)
        output1.writelines(result14)
        output1.writelines(result15)
        line_count += 1
output1.close()  
