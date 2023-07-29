import socket
import struct

def ip_to_u32(ip):
  return int(''.join('%02x' % int(d) for d in ip.split('.')), 16)

SNS_SOURCES = [
    # US-EAST-1
    '207.171.167.101',
    '207.171.167.25',
    '207.171.167.26',
    '207.171.172.6',
    '54.239.98.0/24',
    '54.240.217.16/29',
    '54.240.217.8/29',
    '54.240.217.64/28',
    '54.240.217.80/29',
    '72.21.196.64/29',
    '72.21.198.64/29',
    '72.21.198.72',
    '72.21.217.0/24',
]

for cidr in SNS_SOURCES:
    if '/' in cidr:
        netstr, bits = cidr.split('/')
        mask = (0xffffffff << (32 - int(bits))) & 0xffffffff
        net = ip_to_u32(netstr) & mask
        print ("Got /:", mask, net)
    else:
        mask = 0xffffffff
        net = ip_to_u32(cidr)
        print ("No Mask:", mask, net)

