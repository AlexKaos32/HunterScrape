This is a python script using the hunter.io API to pull data on a target domain, then generate a target email list. This is primarily for password spraying using a tool like Go365 or TREVORspray.

Usage: HunterScrape-Dev.py [-h] -d DOMAIN -k KEY [-l LIMIT]  [-f] [-o OUTFILE]

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Target domain to hunt
  -k KEY, --key KEY     Your hunter.io API key
  -l LIMIT, --limit LIMIT
                        Number of emails to pull, limit 100
  -f, --full            Toggle Full Results
  -o OUTFILE, --outfile OUTFILE
                        Store emails in a text file

Full list example usage:

`./HunterScrape.py -d $targetdomain.org -k $YOUR_API_KEY -f`

If you only want a certain number, up to 100, then use the `-l` flag. Running without specifying `-l N` or `-f` will return a single result.

`./HunterScrape.py -d $targetdomain.org -k $YOUR_API_KEY -l 9`


