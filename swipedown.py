import os, sys, time
import random as r
import socket
from inject import sqlInject, cssInject
from scan import vulnScan
from parameter import httpPollute
from disrupt.deny import ddos, deface
from persist import pingClient as pc, pingServer as ps


class main():
    home = ps.ip
    home_port = ps.port
    host = pc.ip
    hPort = pc.port
    
    f = open('target.json',"r")
    
    
    def init():
        if __name__ == '__main__':
            main()
    
    def start(question):
        
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
            1:vulnScan(),
            2:sqlInject(),
            3:httpPollute(),
            4:cssInject(),
            5:deface(),
            6:ddos()
        }
        return attacks