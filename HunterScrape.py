#!/usr/bin/env python3

import requests, argparse, sys, json, pathlib

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", type=str, required=True, help="Target domain to hunt")
parser.add_argument("-k", "--key", type=str, required=True, help="Your hunter.io API key")
parser.add_argument("-l", "--limit", type=str, default=str(1), help="Number of emails to pull, max 100" )
parser.add_argument("-f", "--full", action='store_true', help="Retrieve all emails")
parser.add_argument("-o", "--outfile", type=str, help="Store emails in a text file")

args = parser.parse_args()

url = "https://api.hunter.io/v2/domain-search?domain="

#This is used to pull the number of emails in order to paginate in the hunter() func
#However it's also used when the -l switch is used to specify a number of emails up to 100
def total_check():
    global obj
    req = ''.join([url, args.domain, "&limit=", args.limit, "&api_key=", args.key])
    hunted = requests.get(req)
    obj = json.loads(hunted.text)
    num_entries = obj["meta"]["results"]
    return num_entries

#This builds the request for the hunter() function.
#I could probably de-dup this and total_check(), but this is how it is for now
def fetch_data(offset):
    global req
    req = ''.join([url, args.domain, "&limit=100","&offset=", str(offset), "&api_key=", args.key])
    fetched = requests.get(req)
    return fetched.json()

#Initialize parameters
def hunter():
    global obj
    total_results = total_check()
    all_emails = []
    offset = 0

    #Loop through requests and extend the list
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

if args.outfile:
    p = pathlib.Path(args.outfile)
    p.write_text('\n'.join(obj["emails"]))
else:
    for email in obj["emails"]:
        print(email)
