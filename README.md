# Whitelist UI
A user interface (Both CLI and Web UI) to access and modify your local whitelist.json (for now) for minecraft servers.

**PIP is required for this to work. It will be pre-installed when you install the latest version of Python.**

Python Version Used: **3.10.6**

Get Python Here: https://www.python.org/downloads/

## Table Of Contents
1. [Introduction](https://github.com/Qazaroth/Whitelist-UI/blob/main/README.md#introduction)
2. [Features](https://github.com/Qazaroth/Whitelist-UI/blob/main/README.md#features)
3. [Planned Features](https://github.com/Qazaroth/Whitelist-UI/blob/main/README.md#TODO)
4. [Running Whitelist UI](https://github.com/Qazaroth/Whitelist-UI/blob/main/README.md#Running-Whitelist-UI)
5. [Bugs & Fixes](https://github.com/Qazaroth/Whitelist-UI/blob/main/README.md#Bugs-and-Fixes)
6. [Contact](https://github.com/Qazaroth/Whitelist-UI/blob/main/README.md#Contact)

## Introduction
A user interface (Both CLI and Web UI) to access and modify your local whitelist.json (for now) for minecraft servers.

## Features
1. Add, remove user(s) from whitelist.json
2. Has both CLI and Web UI which you can specify for your own use

## TODO
- [X] Web Interface
- [ ] Logging system
- [ ] Backup system
- [ ] Allow viewing and/or modification of other files

## Running Whitelist UI
Before even running the program, be sure to install the libraries specified in `requirements.txt`.
For example: `pip install mojang` in a command prompt, powershell or a terminal of your choice.

For Windows Users: You can use the batch file provided. (If it does not work, edit the file and change "python3.10" with "python" or "python3" depending on how your python has been installed) <br>
For Non-Windows Users: You'll have to manually execute the python file yourself.

Here's an example:

Accessing the main page of the server.
1. Start **main.py** or **start.bat**:
    - If starting **main.py**:
        - Open a terminal, navigate to WhitelistUI folder.
        - Type: `python main.py` or `python3 main.py`
    ` If starting **start.bat**, just double click it as you would with any other applications.

2. Once it's running, accessing the page by going to http://127.0.0.1:5000

## Bugs and Fixes
Generally for any error, if it does not resolve itself or not something stupid done by your OS, you can try to redownload from the github and it should work. 

If it  does not, you can start an issue, with the format below:
Title: Issue you're having
Comment:
- Describe your issue
- Describe what you did before
- If possible, provide screenshots
*More information will be needed, do not delete anything*

If **start.bat** does not run the program, edit the batch file and change `python3.10` with your respective python.

## Contact
If you're having an issue with the program, you can just start an issue following the format stated above as best as possible.
