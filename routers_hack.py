import requests
from bs4 import BeautifulSoup
import js2py
from os import system

def get_info(url):
    #Authonticate
    session = requests.session()
    payload = {
        'username': 'admin',
        'password': 'admin'
    }
    session.post(url + '/GponForm/LoginForm', data=payload)

    #Get laninfo page
    page = session.get(url + '/laninfo.html')

    #Extracting JS content
    soup = BeautifulSoup(page.text, 'html.parser')
    js_em_html = str(soup.find_all('script')[3])
    js_cointainer = js_em_html[31:len(js_em_html)-10]

    anime_list = open('test.js', 'w', encoding='utf-8')
    anime_list.write(js_cointainer + '\nconsole.log(WlSsidName)')
    anime_list.close()
    users = system('node test.js')
    return users

def get_info_per_router():
    url = 'http://10.3.1.'
    users_dictionary = {}
    for num in range(2,255):
        try:
            users_dictionary[url+ str(num)] = get_info(url + str(num))
        except:
            continue
        print('Progress: ' + str(num) + ' / 255')
    return users_dictionary

users = get_info_per_router()
print(users)