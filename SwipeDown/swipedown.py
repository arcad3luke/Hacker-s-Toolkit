import json

from SwipeDown.SwipeDown.Inject import sql, css
from SwipeDown.SwipeDown.Parameter import httpPollute
from SwipeDown.SwipeDown.Disrupt.Deny import deface
from SwipeDown.SwipeDown.Scan import google_scrape as webscrape
from SwipeDown.SwipeDown.Persist import pingClient as pc, pingServer as ps
from SwipeDown.destiny import nmap, shodansearch, zdstresser as stresser


# Menu function
class SwipeDown:
    ps.pingServer()
    ping = pc.pingClient()

    # Set the file to write info to
    f = open('target.json', "r")
    json.dump(ping, f)

    def menu(self, ping):
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
                3: sql,
                4: httpPollute,
                5: css,
                6: deface,
                7: stresser
            }
            return attacks
            # Establish host/home vars
    menu(ping)
def init():
    if __name__ == '__main__':
        SwipeDown()

sd = SwipeDown()