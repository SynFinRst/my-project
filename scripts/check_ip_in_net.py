import socket
import struct


def addressInNetwork(ip, net):
    "Is an address in a network"
    ipaddr = struct.unpack('L', socket.inet_aton(ip))[0]
    netaddr, bits = net.split('/')
    netmask = struct.unpack('L', socket.inet_aton(netaddr))[0] & ((2L << int(bits)-1) - 1)
    return ipaddr & netmask == netmask
