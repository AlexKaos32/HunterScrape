#!/usr/bin/env python3

import requests
import argparse
import sys
import json
from operator import itemgetter

#Using Argparse to specify cli arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", type=str, required=True, help="Target domain to hunt")
parser.add_argument("-k", "--key", type=str, required=True, help="Your hunter.io API key")
args = parser.parse_args()

#Request info from
url = "https://api.hunter.io/v2/domain-search?domain="
req = ''.join([url, args.domain, "&limit=100", "&api_key=", args.key])
hunted = requests.get(req)

#Output results to file to parse here, and further analysis
with open ("hunted.json", "w") as f:
    f.write((hunted.text))

#Opening the output data
huntFile = open('hunted.json','r')
jdata = huntFile.read()

#Parsing for emails
obj=json.loads(jdata)
entries = obj["data"]["emails"]

bounty = list(map(itemgetter('value'), entries))

print(str(bounty))
