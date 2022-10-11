def shodansearcher():
    import shodan
    SHODAN_API_KEY = "REDACTED"
    api = shodan.Shodan(SHODAN_API_KEY)
    search = input("Query:")
    results = api.search(search)
    print('Results found: {}'.format(results['total']))
    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        print(result['data'])
        print('')
