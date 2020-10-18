#!/usr/bin/env python

import subprocess
import optparse
import re


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
    print("[+] Changing MAC address for " + interface + " to: " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address:
        return mac_address.group(0)
    else:
        print("[-] Could not read MAC address")


option = get_arguments()

current_mac = get_current_mac(option.interface)
print("Previous MAC address: " + str(current_mac))

change_mac(option.interface, option.new_mac)

current_mac = get_current_mac(option.interface)
if current_mac == option.new_mac:
    print("[+] Successfully changed MAC address to " + str(current_mac))
else:
    print("[-] MAC address not changed")
