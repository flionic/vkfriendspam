import requests

vk_api = 'https://api.vk.com/method/'
vk_cfg = '&v=5.64' + '&access_token='
settings_conf = {}
target_ulist = {}


def get_settings():
    global settings_conf
    try:
        file_cfg = open('settings.cfg', 'r+')
        settings_conf = [line.strip() for line in file_cfg]
        print(f'Target link: {settings_conf[0]}')
    except FileNotFoundError:
        print('Settings file not found, please run install')
    except Exception as excp:
        print(f'Error while get settings: {excp}')
get_settings()


def verify_bots():
    for i in range(1, len(settings_conf)):
        try:
            r = requests.get(vk_api + 'account.getProfileInfo?' + vk_cfg + settings_conf[i]).json()
            print(f"Bot {i}: {r['response']['first_name']} {r['response']['last_name']}")
        except:
            print(f"Bot {i}: {r['error']['error_msg']}")
verify_bots()


def get_type(target):
    try:
        target = target[target.find('vk.com/'):].strip('vk.com/')
        vk_resp = requests.get(vk_api + 'utils.resolveScreenName?screen_name=' + target + vk_cfg + settings_conf[1]).json()
        _type = vk_resp['response']['type']
        _id = vk_resp['response']['object_id']
        print(f'Type: {_type}')
    except IndexError:
        print('Bots not found')
    except Exception as excp:
        print(f'Error while get link type: {excp}')
get_type('https://vk.com/bionic.leha')
