#!/usr/bin/env python3

import requests, argparse, sys, json
from operator import itemgetter

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", type=str, required=True, help="Target domain to hunt")
parser.add_argument("-k", "--key", type=str, required=True, help="Your hunter.io API key")
parser.add_argument("-l", "--limit", type=str, help="Number of emails to pull, limit 100" )
parser.add_argument("-f", "--full", action='store_true', help="Toggle Full Results")
args = parser.parse_args()

url = "https://api.hunter.io/v2/domain-search?domain="

def total_check():
    global obj
    req = ''.join([url, args.domain, "&limit=", args.limit, "&api_key=", args.key])
    hunted = requests.get(req)
    obj = json.loads(hunted.text)
    num_entries = obj["meta"]["results"]
    return num_entries

def fetch_data(offset):
    global req
    req = ''.join([url, args.domain, "&limit=100","&offset=", str(offset), "&api_key=", args.key])
    fetched = requests.get(req)
    return fetched.json()

def hunter():
    global obj
    total_results = total_check()
    all_emails = []
    offset = 0

    while offset < total_check():
        data = fetch_data(offset)
        emails = [email['value'] for email in data["data"]["emails"]]
        all_emails.extend(emails)
        offset += 100

    obj["emails"] = all_emails
    return obj
    

if args.full:
    hunter()
else:
    total_check()
    obj["emails"] = [email['value'] for email in obj["data"]["emails"]]

for email in obj["emails"]:
    print(email)
