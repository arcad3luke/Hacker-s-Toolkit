import socket as s
import dpkt, re, urllib,  getopt
import subprocess, os, platform, sys
from SwipeDown.SwipeDown.persist import pingClient as pc
from SwipeDown.SwipeDown.payload.Python_Reverse_TCP import reverse_tcp

class sqlInject(reverse_tcp):
    tab = False
    """"
    learn sql injection and make a script for it. 
    @TODO
    
    """


    def removecomments(self, val):
        while True:
            index = val.find("/*")
            index2 = val.find("*/")
            if index != -1 and index2 != -1:
                remove = val[index:index2+2]
                val = val.replace(remove, "")
            else:
                break
        return val
    