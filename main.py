from config import *

from FileHandler import FileHandler
from WhitelistHandler import WhitelistHandler
from flask import Flask
from MCAPI import *

fileHandler = FileHandler()
whHandler = WhitelistHandler()

def createApp():
    app = Flask(__name__)
    app.secret_key = ""

    with app.app_context():
        import blueprints.index

        app.register_blueprint(blueprints.index.bp)

        return app

if __name__ == "__main__":
    if not isCLI:
        app = createApp()
        
        app.run(port=webPort)
    else:
        from Utils import clear

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
            removeMore = True

            while removeMore:
                clear()
                print("""
                Q in any of the input to stop.""")

                username = input("Username of Player you want to remove (Case Sensitive): ")
                if username.lower() == "q":
                    removeMore = False
                    break

                isSuccess = whHandler.removeFromWhitelist(username)
                if isSuccess:
                    print("Successfully removed {} to whitelist.".format(username))
                else:
                    print("Error occured while trying to remove {} from whitelist!".format(username))

                toContinue = input("Continue removing players? (Y/N) ")
                toContinue = toContinue.lower()

                removeMore = toContinue == "y"

            whHandler.updateWhitelist()
        else:
            exit()