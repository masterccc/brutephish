import requests
import random
import time
import sys

DELAY           = 0     # Delay between requests, ignored if DELAY_RAND is True
DELAY_RAND      = False # Enable random delay
DELAY_RAND_MIN  = 1     # min time to wait
DELAY_RAND_MAX  = 3     # max time to wait
COUNT           = 1000  # Requests to send
URL             = 'https://***/submit.php'

# Edit **CHANGEME** below before run

_UA = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12 Version/12.16",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML like Gecko) Chrome/23.0.1271.95 Safari/537.11",
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/31.0.1650.63 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/37.0.2062.120 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML like Gecko) Chrome/23.0.1271.95 Safari/537.11",
    "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"
]

print("Loading logins ...")
logins = open("usernames.txt","r", encoding='utf-8', errors='ignore').readlines()
#From https://github.com/jeanphorn/wordlist/


print("Loading passwords ...")
passs = open("top1000pass.txt","r", encoding='utf-8', errors='ignore').readlines()
# From https://github.com/danielmiessler/SecLists/tree/master/Passwords
count = 0

def get_login():
    global logins
    login = random.choice(logins).rstrip()

    # Randomly adds numbers ad the end of login
    if( random.randint(1,2) == 1):
        login += str(random.randint(1,100))
    return login

def get_pass():
    global passs
    passw = random.choice(passs).rstrip()
    passw += random.choice(passs).rstrip()

    # Randomly adds number ad the end
    if( random.randint(1,2) == 1):
        passw += str(random.randint(1,100000))
    
    # Randomly Capitalize the first letter
    if( random.randint(1,2) == 1):
        passw = passw.capitalize()
    return passw


for i in range(1,COUNT):
    count += 1
    headers = {
        'User-Agent': random.choice(_UA),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://**CHANGEME**',
        'Content-Type': 'application/x-www-form-urlencoded',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }

    data = {
        'action': '**CHANGEME**',
        '**LOGIN_CHANGEME**': get_login(),
        '**PASSWORD_CHANGEME**': get_pass()
    }
    
    if((count % 50 == 0)):
        print()
        print("count :", count, data['login']+':' +data['password'])

    response = requests.post(URL, headers=headers, data=data, allow_redirects=False)
    print('.', end='')
    sys.stdout.flush()

    if(DELAY_RAND):
        time.sleep(random.randint(DELAY_RAND_MIN,DELAY_RAND_MAX))
    else:
        time.sleep(DELAY)
