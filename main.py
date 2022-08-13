from config import *

from FileHandler import FileHandler
from WhitelistHandler import WhitelistHandler
from Utils import *
from MCAPI import *

fileHandler = FileHandler()
whHandler = WhitelistHandler()


def cli():
    print("""
        What would you like to do?
        \n0 - Exit
        \n1 - Fetch current whitelist data
        \n2 - Add to whitelist
        \n3 - Remove from whitelist
        """)
    choice = input()

    try:
        choice = int(choice)
    except:
        choice = 1

    if choice == 1:
        clear()
        whHandler.listWhitelistData()
    elif choice == 2:
        addMore = True

        while addMore:
            clear()
            print("""
            Q in any of the input to stop.""")

            username = input("Username of Player you want to add (Case Sensitive): ")

            if username.lower() == "q":
                addMore = False
                break

            isSuccess = whHandler.addToWhitelist(username)

            if isSuccess:
                print("Successfully added {} to whitelist.".format(username))
            else:
                print("Error occured while trying to add {} to whitelist!".format(username))

            toContinue = input("Continue adding more players? (Y/N) ")
            toContinue = toContinue.lower()

            addMore = toContinue == "y"
        
        whHandler.updateWhitelist()
    elif choice == 3:
        clear()
        addMore = True

        while addMore:
            clear()
            print("""
            Q in any of the input to stop.""")

            username = input("Username of Player you want to remove (Case Sensitive): ")
            if username.lower() == "q":
                addMore = False
                break

            isSuccess = whHandler.removeFromWhitelist(username)
            if isSuccess:
                print("Successfully removed {} to whitelist.".format(username))
            else:
                print("Error occured while trying to remove {} from whitelist!".format(username))

            toContinue = input("Continue removing players? (Y/N) ")
            toContinue = toContinue.lower()

            addMore = toContinue == "y"

        whHandler.updateWhitelist()
    else:
        exit()

if __name__ == "__main__":
    cli()