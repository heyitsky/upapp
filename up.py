from upapp.api_client import APIClient
from upapp.account import Account
from upapp.json_handler import JSONHandler
from upapp.auth import get_auth_info

account_list = []

def display_menu():
    """Function to display menu for CLI use"""
    
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

def requestBuilder(destination, *args):
    """Function used to build requests with a given endpoint
    
    Currently servicing:
    - "ping"
    - "accounts"
    - default("ping")
    """

    match(destination):
        case "ping":
            location = "/util/ping"
        case "accounts":
            location = "/accounts"
        case _:
            location = "/util/ping"
 
def test_api(client):
    """Helper function to test API connection using the util/ping endpoint"""

    # request = requests.get(BASE_URL+'/util/ping', headers={"Authorization": "Bearer " + AUTH_TOKEN}
    resp = client.get("util/ping")
    print(resp['meta']['statusEmoji'])

def get_transactions(client, json_hanlder):
    """Function to get a list of transactions"""
    
    resp = client.get("accounts")
    data_list = json_hanlder.get_data(resp)
    account_list.clear()
    if len(data_list) > 0:
        for account in data_list:
            add_account(account)
    
    counter = 1
    print(len(account_list))
    for account in account_list:
        print(f"{counter}. {account.emoji.strip()} {account.name}")
        counter+= 1
    print("0. Exit")

def view_transactions(client, json_hanlder, id):
    """Function used to print transactions for a specific account to the CLI.
    
    an account ID is passed in (handled by menu selection)"""

    resp = client.get(f"accounts/{id}/transactions")
    data_list = json_hanlder.get_data(resp)
    for transaction in data_list:
        print(f'{transaction["attributes"]["settledAt"][:10]} - ${transaction["attributes"]["amount"]["value"]}: {transaction["attributes"]["description"]}')

def get_accounts(client, json_handler):
    """Function used to get a list of accounts and print them to the CLI"""
    
    resp = client.get("accounts")
    data_list = json_handler.get_data(resp)
    account_list.clear()
    if len(data_list) > 0:
        for account in data_list:
            add_account(account)
    for account in account_list:
        # print(account)
        print(f"{account.emoji.strip()} {account.name} - ${account.balance}")

def add_account(account):
    """Helper function used to add Account objects to a list of accounts

    Keeps track of:
    - ID
    - displayName
    - ownershipType
    - value 
    """
    account_list.append(Account(account["attributes"]["accountType"],
                        account["id"],
                        account["attributes"]["displayName"],
                        account["attributes"]["ownershipType"],
                        account["attributes"]["balance"]["value"]))

def main():
    """What are you doing here? 🤔"""
    
    auth_info = get_auth_info()
    client = APIClient(auth_info[0], auth_info[1])
    json_handler = JSONHandler()
    while True:
        display_menu()
        choice = input('')
        match(choice):
            case "1":
                print('---------------------------------------------------------------')
                get_accounts(client, json_handler)
                # print("view account working!")
                input('Press enter to continue...')
            
            case "2":
                print('---------------------------------------------------------------')
                # TODO - better handling of this, potential error
                get_transactions(client, json_handler)
                # print("view transactions working!")
                while True:
                    try:
                        choice = int(input("Choose an account with the corresponding number: "))
                        if not choice < len(account_list)+1:
                            raise ValueError("No account matches that number in the list above.")
                        break
                    except ValueError:
                        print("Invalid input! Please enter an integer")

                while choice != 0:
                    print(f"{account_list[choice-1].name} was chosen!")
                    account = account_list[choice-1]

                    break
                    # match choice to corresponding account in length
                input('Press enter to continue...')
                view_transactions(client, json_handler, account.id)
                input('Press enter to continue...')
            
            case "3":
                print('---------------------------------------------------------------')
                test_api(client)
                # print("test api working!")
                input('Press enter to continue...')
            
            case "4":
                print("Bye for now!")
                break

            case _:
                print('---------------------------------------------------------------')
                print("Invalid option! Please select from the menu")
                input('Press enter to continue...')

if __name__ == "__main__":
    main()