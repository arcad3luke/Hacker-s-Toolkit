import nmap3
import json

nmap = nmap3.Nmap()


def menu():
    print("""          _______  _        _______  _______  _______  _______ 
|\     /|(  ____ \( \      (  ____ \(  ___  )(       )(  ____ \
| )   ( || (    \/| (      | (    \/| (   ) || () () || (    \/
| | _ | || (__    | |      | |      | |   | || || || || (__    
| |( )| ||  __)   | |      | |      | |   | || |(_)| ||  __)   
| || || || (      | |      | |      | |   | || |   | || (      
| () () || (____/\| (____/\| (____/\| (___) || )   ( || (____/\
(_______)(_______/(_______/(_______/(_______)|/     \|(_______/""")
    choose = input("""Which tool would you like to use?

[1] OS Detection
[2] DNS scan
[3] Version detection
[4] Scan top ports
[5] Scan all

Tool:""")
    if choose == "1":
        nmapos()
    elif choose == "2":
        nmapdns()
    elif choose == "3":
        nmapversion()
    elif choose == "4":
        nmapports()
    elif choose == "5":
        nmapall()


def nmapos():
    target = input("\nTarget: ")
    print(f"\nScanning {target}, please wait...")
    os_results = nmap.nmap_os_detection(target)
    print(json.dumps(os_results, indent=4, sort_keys=True))


def nmapdns():
    target = input("Target: ")
    print(f"\nScanning {target}, please wait...")
    dns_results = nmap.nmap_dns_brute_script(target)
    print(json.dumps(dns_results, indent=4, sort_keys=True))


def nmapversion():
    target = input("Target: ")
    print(f"\nScanning {target}, please wait...")
    version_results = nmap.nmap_version_detection(target)
    print(json.dumps(version_results, indent=4, sort_keys=True))


def nmapports():
    target = input("Target: ")
    print(f"\nScanning {target}, please wait...")
    ports = nmap.scan_top_ports(target)
    print(json.dumps(ports, indent=4, sort_keys=True))


def nmapall():
    nmap = nmap3.Nmap()
    target = input("Target: ")
    print("\nScanning, please wait: " + target)
    print("\nDetecting os...")
    os_results = nmap.nmap_os_detection(target)
    print("\nSuccess!! Scanning dns...")
    dns_results = nmap.nmap_dns_brute_script(target)
    print("\nSuccess!! Detecting version...")
    version_results = nmap.nmap_version_detection(target)
    print("\nSuccess!! Scanning top ports...")
    ports = nmap.scan_top_ports(target)
    print("\nSuccess! All scans finished, compiling results...")
    print(json.dumps(os_results, indent=4, sort_keys=True))
    print(json.dumps(dns_results, indent=4, sort_keys=True))
    print(json.dumps(version_results, indent=4, sort_keys=True))
    print(json.dumps(ports, indent=4, sort_keys=True))


menu()
