import requests

try:
    users = open('settings.cfg', 'r+')
    users.close()
    users = open('settings.cfg', 'a')
    u_login = input('VK Login: ')
    u_pass = input('VK Password: ')
    try:
        login = requests.get(f'https://oauth.vk.com/token?grant_type=password&scope=friends&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username={u_login}&password={u_pass}').json()
        print('Successful')
        users.write(login['access_token'] + '\n')
        users.close()
    except:
        print('Error while login')
except FileNotFoundError:
    print('Settings file not found, please run install')
