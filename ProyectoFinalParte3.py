#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
from os import sys

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='191.4.199.0/24')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=Controller,
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h6 = net.addHost('h6', cls=Host, ip='191.4.199.6', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='191.4.199.4', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='191.4.199.8', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='191.4.199.9', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='191.4.199.7', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='191.4.199.5', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='191.4.199.2', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='191.4.199.1', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='191.4.199.3', defaultRoute=None)


    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')



    info( '*** Post configure switches and hosts\n')


    net.stop()
    exit()
    	
	
if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()



