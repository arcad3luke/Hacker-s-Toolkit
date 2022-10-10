import re

def urlRegex():
    url_decode = re.search('/[A-Za-z]+:\/\/[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_:%&;\?\#\/.=]+/g')
    with open('url_decoded_regex.txt', 'w') as f:
        decoded_file = url_decode.split('')
        f.close(decoded_file)
    