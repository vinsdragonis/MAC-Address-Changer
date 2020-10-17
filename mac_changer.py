#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="use this to set network interface")
parser.add_option("-m", "--mac", dest="new_mac", help="use this to set new MAC address for the network interface")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("Changed MAC address for " + interface + " is set to = " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
