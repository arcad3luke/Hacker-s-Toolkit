import json

from inject import sqlInject, cssInject
from parameter import httpPollute
from disrupt.deny import ddos, deface
from scan import google_scrape as webscrape
from persist import pingClient as pc, pingServer as ps


# Menu function
def on_start(ping):
    question = input('''
        Available methods of attack are as follows:\n
        1) Web Scrape & Scan\n
        2) SQL Injection\n
        3) HTTP Parameter Pollution\n
        4) CSS Injection\n
        5) Deface\n
        6) DDoS\n
        Select Attack Method: ''')
    yield question

    if ping:
        attacks = {
            1: webscrape,
            2: sqlInject,
            3: httpPollute,
            4: cssInject,
            5: deface,
            6: ddos
        }

        return attacks


class Main:
    # Establish host/home vars
    ps.pingServer()
    ping = pc.pingClient()

    # set the file to write info to
    f = open('target.json', "r")
    json.dump(ping, f)
    on_start(ping)


# Start
def init():
    if __name__ == '__main__':
        Main()
