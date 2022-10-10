import json
import os
import swipedown as sd
from persist import pingClient as pc
class vulnScan():

    Set = range(1, 255)
    randomIP = (f'{Set}.{Set}.{Set}.{Set}')
    version = 0
    scan = os.command(
        f'nmap -p- -v -sV --script=vulners.nse -f -Pn -T4 -o sd_scan_{version}.txt' + randomIP)
    version += 1
    