import time
import requests

vk_api = 'https://api.vk.com/method'
vk_cfg = '&v=5.64' + '&access_token='
settings_conf = {}
target_ulist = []


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
            r = requests.get(f'{vk_api}/account.getProfileInfo?' + vk_cfg + settings_conf[i]).json()
            print(f"Bot {i}: {r['response']['first_name']} {r['response']['last_name']}")
        except:
            print(f"Bot {i}: {r['error']['error_msg']}")
verify_bots()


def get_type(target):
    try:
        target = target[target.find('vk.com/'):].strip('vk.com/')
        vk_resp = requests.get(f'{vk_api}/utils.resolveScreenName?screen_name=' + target + vk_cfg + settings_conf[1]).json()
        _type = vk_resp['response']['type']
        _id = vk_resp['response']['object_id']
        if _type == 'user':
            get_friends(_id)
        elif _type == 'group':
            get_members(_id)
    except IndexError:
        print('Bots not found')
    except Exception as excp:
        print(f'Error while get link type: {excp}')


def get_friends(_id):
    global target_ulist
    try:
        print('Get user friends...')
        ulist = requests.get(f'{vk_api}/friends.get?order=random&user_id={_id}').json()
        target_ulist = ulist['response']
    except Exception as excp:
        print(f'Error while get friends: {excp}')


# Feature
def get_members(_id):
    global target_ulist
    try:
        print('Get group members...')
        ulist = requests.get(f'{vk_api}/groups.getMembers?count=0&group_id={_id}').json()
        members_count = ulist['response']['count']
        if (members_count % 1000) > 0:
            reqs_nums = (members_count / 1000) + 1
        else:
            reqs_nums = members_count / 1000
        for i in range(0, int(reqs_nums)):
            ulist = requests.get(f'{vk_api}/groups.getMembers?offset={i*1000}&group_id={_id}{vk_cfg}').json()
            target_ulist += (ulist['response']['items'])
            time.sleep(0.2)
    except Exception as excp:
        print(f'Error while get members: {excp}')

get_type('https://vk.com/worket')
