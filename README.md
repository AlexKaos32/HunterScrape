This is a python script using the hunter.io API to pull data on a target domain, then generate a target email list. By default, this only returns up to 100 emails.
For now if you need more than 100, edit line 17 to reflect the following:
`req = ''.join([url, args.domain, "&limit=100", "&offset=N", "&api_key=", args.key])`

Where `N` is the number of emails you want to skip collecting. For example, if you need to get 200 emails, set the offset to 100 on the second run to skip the first 100 emails you've already gathered.



Requirements: 

`python3 -m pip uninstall pyppeteer pyee`

`python3 -m pip install --upgrade urllib3`

`python3 -m pip install pyhunter`

To Do: Add an option for offset parameter to allow getting all emails.
