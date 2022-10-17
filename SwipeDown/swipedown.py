from SwipeDown.SwipeDown.inject import sqlInject, cssInject
from SwipeDown.SwipeDown.parameter import httpPollute
from SwipeDown.SwipeDown.disrupt.deny import ddos, deface
from SwipeDown.SwipeDown.persist import pingClient as pc, pingServer as ps


class Main:
    # Establish host/home vars
    ps.pingServer()

    # set the file to write info to
    f = open('target.json', "r")

    # Menu function
    def on_start(self, question):
        question = input('''
            Available methods of attack are as follows:\n
            1) Vuln Scan\n
            2) SQL Injection\n
            3) HTTP Parameter Pollution\n
            4) CSS Injection\n
            5) Deface\n
            6) DDoS\n
            Select Attack Method: ''')
        yield question

        ping = pc.pingClient()
        if ping:
            attacks = {
                1: sqlInject,
                2: httpPollute,
                3: cssInject,
                4: deface,
                5: ddos
            }

            return attacks

# Start
def init():
    if __name__ == '__main__':
        Main()
