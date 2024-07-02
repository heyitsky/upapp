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
                # viewAccountMenu()
                print("view account working!")
                input('Press enter to continue...')
            
            case "2":
                print('---------------------------------------------------------------')
                # viewAccountTransactions()
                print("view transactions working!")
                input('Press enter to continue...')
            
            case "3":
                print('---------------------------------------------------------------')
                # testAPI()
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


if __name__ == "__main__":
    menu()