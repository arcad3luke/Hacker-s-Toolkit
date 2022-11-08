import json

from inject import sqlInject, cssInject
from parameter import httpPollute
from disrupt.deny import deface
from scan import google_scrape as webscrape
from persist import pingClient as pc, pingServer as ps
from SwipeDown.destiny import nmap, shodansearch, zdstresser


# Menu function
def menu(ping):
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
    if ping:
        attacks = {
            1: webscrape,
            2: nmap,
            3: sqlInject,
            4: httpPollute,
            5: cssInject,
            6: deface,
            7: zdstresser
        }
        return attacks

class Main:
    # Establish host/home vars
    ps.pingServer()
    ping = pc.pingClient()

    # Set the file to write info to
    f = open('target.json', "r")
    json.dump(ping, f)
    menu(ping)

# Start
def init():
    if __name__ == '__main__':
        Main()