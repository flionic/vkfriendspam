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
        print(settings_conf)
    except FileNotFoundError:
        print('Settings file not found, please run install')
    except Exception as excp:
        print(excp)
get_settings()


def verify_bots():
    for i in range(1, len(settings_conf)):
        try:
            r = requests.get(vk_api + 'account.getProfileInfo?' + vk_cfg + settings_conf[i]).json()
            print(f"Bot {i}: {r['response']['first_name']} {r['response']['last_name']}")
        except:
            print(f"Bot {i}: {r['error']['error_msg']}")
verify_bots()
