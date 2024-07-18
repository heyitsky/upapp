from upapp.api_client import APIClient
from upapp.account import Account
from upapp.json_handler import JSONHandler
from upapp.auth import get_auth_info

account_list = []

def display_menu():
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
    match(destination):
        case "ping":
            location = "/util/ping"
        case "accounts":
            location = "/accounts"
        case _:
            location = "/util/ping"

def test_api(client):
    # request = requests.get(BASE_URL+'/util/ping', headers={"Authorization": "Bearer " + AUTH_TOKEN}
    resp = client.get("util/ping")
    print(resp['meta']['statusEmoji'])

def get_transactions(client, json_hanlder):
    resp = client.get("accounts")
    data_list = json_hanlder.get_data(resp)
    account_list.clear()
    if len(data_list) > 0:
        for account in data_list:
            add_account(account)
    counter = 1
    for account in account_list:
        print(f"{counter}. {account.emoji.strip()} {account.name}")
        counter+= 1
    print("0. Exit")
    return len(account_list)

def get_accounts(client, json_handler):
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
    account_list.append(Account(account["attributes"]["accountType"],
                        account["id"],
                        account["attributes"]["displayName"],
                        account["attributes"]["ownershipType"],
                        account["attributes"]["balance"]["value"]))

def main():
    auth_info = get_auth_info()
    client = APIClient(auth_info[0], auth_info[1])
    json_handler = JSONHandler()
    display_menu()
    choice = input('')
    while choice != "4":
        match(choice):
            case "1":
                print('---------------------------------------------------------------')
                get_accounts(client, json_handler)
                # print("view account working!")
                input('Press enter to continue...')
            
            case "2":
                print('---------------------------------------------------------------')
                # TODO - better handling of this, potential error
                number_of_accounts = get_transactions(client, json_handler)
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
                    print(f"{account_list[choice].name} was chosen!")
                    break
                    # match choice to corresponding account in length
                input('Press enter to continue...')
            
            case "3":
                print('---------------------------------------------------------------')
                test_api(client)
                # print("test api working!")
                input('Press enter to continue...')
            
            case _:
                print('---------------------------------------------------------------')
                print("Invalid option! Please select from the menu")
                input('Press enter to continue...')

        display_menu()
        choice = input('')
        print("Bye for now!")

if __name__ == "__main__":
    main()