from inject import sqlInject, cssInject
from parameter import httpPollute
from disrupt.deny import ddos, deface
from persist import pingClient as pc, pingServer as ps


class Main:
    home = ps.ip
    home_port = ps.port
    host = pc.ip
    hPort = pc.port

    f = open('target.json', "r")

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
            1: sqlInject(),
            2: httpPollute(),
            3: cssInject(),
            4: deface(),
            5: ddos()
        }
        return attacks


def init():
    if __name__ == '__main__':
        Main()
