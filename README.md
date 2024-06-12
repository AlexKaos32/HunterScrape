This is a python script using the hunter.io API to pull data on a target domain, then generate a target email list. This is primarily for password spraying using a tool like Go365 or TREVORspray.


Full List Example Usage:

`./HunterScrape.py -d $targetdomain.org -k $YOUR_API_KEY -f`

If you only want a certain number, up to 100, then use the `-l` flag:

`./HunterScrape.py -d $targetdomain.org -k $YOUR_API_KEY -l 9`
