import nmap,shodansearch,zdstresser

def menu1():
    print("""          _______  _        _______  _______  _______  _______ 
|\     /|(  ____ \( \      (  ____ \(  ___  )(       )(  ____ \
| )   ( || (    \/| (      | (    \/| (   ) || () () || (    \/
| | _ | || (__    | |      | |      | |   | || || || || (__    
| |( )| ||  __)   | |      | |      | |   | || |(_)| ||  __)   
| || || || (      | |      | |      | |   | || |   | || (      
| () () || (____/\| (____/\| (____/\| (___) || )   ( || (____/\
(_______)(_______/(_______/(_______/(_______)|/     \|(_______/\n""")
    main = input("""Which tool would you like to use?

[1] Nmap
[2] Shodan Scraper
[3] ZDstresser DDos toolkit (requires API key, read the py file)

Tool:""")
    if main == "1":
        nmap.menu()
    if main == "2":
        shodansearch.main()
    if main == "3":
        zdstresser.main()

