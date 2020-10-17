#!/usr/bin/env python

import subprocess

interface = input("interface\n>")
newMac = input("address\n>")

print("Changed MAC address for " + interface + " is set to = " + newMac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw","ether", newMac])
subprocess.call(["ifconfig", interface, "up"])
