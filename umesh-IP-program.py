DICT ={10.234.136.55:2,
        10.234.137.55:1}
'This line corresponds to ip address 10.234.136.55'
'This line ip address 10.234.154.55'
'This line ip address 10.234.153.55'
'This line corresponds to ip address 10.234.137.55'
'This line corresponds to ip address 10.234.136.55'

filename='ipsaddresses.txt'
    for line in open(filename,'r'):
        if 'corersponds to' in line:
            ip_address = line.split(' ')[6]
            if DICT[ip_address] > 0:
                DICT[ip_address] = DICT[ip_address] + 1
            else:
                DICT.append(ip_address:1)
for ip_address,value in DICT:
    print('ip address = ',key,'count = ',value)

ip address = 10.234.136.55 count = 2
ip address = 10.234.137.55 count = 1

10.234.136.55:4