# upapp
A desktop app using Up Bank's API

## Dependencies:
Required:
- requests
- os

Optional:
- dotenv

## Bugs/Changes to be Made:
- Add option to use .env for token or access token from file
- Add error handling for requests (test for response codes)
- Create account class, store id, type, name, value, trans?
- Refactor Account to own file
- Refactor Requests to own file
- Refactor JSONHandler to own file
- Load in accounts on program start?