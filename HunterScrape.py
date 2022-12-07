#!/usr/bin/env python3

from pyhunter import PyHunter
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--domain", type=str, required=True, help="Target domain to hunt")
parser.add_argument("-k", "--key", type=str, required=True, help="Your hunter.io API key")
args = parser.parse_args()

hkey = PyHunter(args.key)
info = hkey.domain_search(args.domain)

print (info)
