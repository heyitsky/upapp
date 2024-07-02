from dotenv import load_dotenv
import requests
import os

load_dotenv(dotenv_path='./auth.env')

BASE_URL = "https://api.up.com.au/api/v1/"
AUTH_TOKEN = os.getenv('API_TOKEN')

def menu():
    print("Desktop Up Bank App!")
    print("----------------------")
    print(
"""Choose an item from the following menu using the number:
---------------------------------------------------------------
1. | View Account Balance
2. | View Account Transactions
3. | Test API
4. | Exit""")
    print('---------------------------------------------------------------')
    choice = input('') 
    while choice != "4":
        match(choice):
            case "1":
                print('---------------------------------------------------------------')
                viewAccounts()
                print("view account working!")
                input('Press enter to continue...')
            
            case "2":
                print('---------------------------------------------------------------')
                # viewAccountTransactions()
                print("view transactions working!")
                input('Press enter to continue...')
            
            case "3":
                print('---------------------------------------------------------------')
                testAPI()
                print("test api working!")
                input('Press enter to continue...')
            
            case _:
                print('---------------------------------------------------------------')
                print("Invalid option! Please select from the menu")
                input('Press enter to continue...')

        print('---------------------------------------------------------------')
        print(
        """Choose an item from the following menu using the number:
---------------------------------------------------------------
1. | View Account Balance
2. | View Account Transactions
3. | Test API
4. | Exit""")
        choice = input('')
    print("Bye for now!")

def requestBuilder(destination, *args):
    match(destination):
        case "ping":
            location = "/util/ping"
        case "accounts":
            location = "/accounts"
        case _:
            location = "/util/ping"
    # have a switch which adds destination based off of function calling it i.e. accounts
    request = requests.get(BASE_URL+location, headers={"Authorization": "Bearer " + AUTH_TOKEN})
    return request.json()

def testAPI():
    # request = requests.get(BASE_URL+'/util/ping', headers={"Authorization": "Bearer " + AUTH_TOKEN})
    request = requestBuilder("ping")
    print(request['meta']['statusEmoji'])

def viewAccounts():
    request = requestBuilder("accounts")
    print(request)

if __name__ == "__main__":
    menu()