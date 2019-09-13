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

    info( '*** Add links\n')
    net.addLink(h1, s1, cls=TCLink, bw=10, delay=5)
    net.addLink(s1, s2, cls=TCLink, bw=5, delay=10)
    net.addLink(s2, s7, cls=TCLink, bw=7, delay=20)
    net.addLink(s7, s8, cls=TCLink, bw=3, delay=4)
    net.addLink(s2, s3, cls=TCLink, bw=5, delay=1)
    net.addLink(s3, s4, cls=TCLink, bw=4, delay=50)
    net.addLink(s8, s5, cls=TCLink, bw=6, delay=40)
    net.addLink(s5, s6, cls=TCLink, bw=20, delay=0)
    net.addLink(s5, h6, cls=TCLink, bw=1, delay=1000)
    net.addLink(s5, h7, cls=TCLink, bw=1, delay=98)
    net.addLink(s6, h8, cls=TCLink, bw=4, delay=14)
    net.addLink(s6, h9, cls=TCLink, bw=3, delay=25)
    net.addLink(s3, h2, cls=TCLink, bw=10, delay=65)
    net.addLink(s3, h3, cls=TCLink, bw=2, delay=52)
    net.addLink(s4, h4, cls=TCLink, bw=5, delay=54)
    net.addLink(s4, h5, cls=TCLink, bw=1, delay=2)


    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s4').start([c0])
    net.get('s7').start([c0])
    net.get('s1').start([c0])
    net.get('s3').start([c0])
    net.get('s8').start([c0])
    net.get('s6').start([c0])
    net.get('s2').start([c0])
    net.get('s5').start([c0])

    net.pingAll()

    info( '*** Post configure switches and hosts\n')


    net.stop()
    exit()
    	
	
if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()



