#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="use this to set network interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="use this to set new MAC address for the network interface")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        # error handling for no interface condition
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        # error handling for no mac condition
        parser.error("[-] Please specify a new MAC address, use --help for more info")

    return options


def change_mac(interface, new_mac):
    print("Changed MAC address for " + interface + " is set to = " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


option = get_arguments()
change_mac(option.interface, option.new_mac)
