import json

from SwipeDown.SwipeDown.Inject import sql, css
from Parameter import httpPollute
from Disrupt.Deny import deface
from Scan import google_scrape as webscrape
from Utility.Shell import shell_server as shell
from UI import UI
from SwipeDown.destiny import nmap, shodansearch, zdstresser

global client, port

class Main:

    # Establish host/home vars
    client = input('Enter IP of client: \n')
    port = shell.PORT

    def menu(client):
        question = input('''
            Available methods of attack are as follows:\n
            1) Web Scrape\n 
            2) Nmap Scan\n
            3) SQL Injection\n
            4) HTTP Parameter Pollution\n
            5) CSS Injection\n
            6) Deface\n
            7) Stress Test\n
            Select Attack Method: ''')
        yield question

        # Define menu options
        if client:
            attacks = {
                1: webscrape,
                2: nmap,
                3: sql,
                4: httpPollute,
                5: css,
                6: deface,
                7: zdstresser
            }
            return attacks

    # Initialize UI
    UI.UI()
    # Set the file to write info to
    f = open('clients.json', "r")
    json.dump(client, f)


# Start
def init():
    if __name__ == '__main__':
        Main.menu(client)
