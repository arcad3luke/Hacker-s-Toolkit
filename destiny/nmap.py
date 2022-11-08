import nmap3
import json


def nmapscanner():
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


nmapscanner()
    