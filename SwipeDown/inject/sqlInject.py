import socket as s
import dpkt, re, urllib, sys, getopt
from persist import pingClient as pc
class sqlInject():
    tab = False
    def removeComments(val):
        while True:
            index = val.find("/*")
            index2 = val.find("*/")
            if index != -1 and index2 != -1:
                remove = val[index:index2+2]
                val = val.replace(remove, "")
            else:
                break
        return val
    