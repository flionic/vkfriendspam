import time
import requests
import sqlite3
from urllib.request import urlretrieve
from antigate import AntiGate

vk_api = 'https://api.vk.com/method'
vk_cfg = '&v=5.64' + '&access_token='
settings_conf = {}
bots_list = []


def get_settings():
    global settings_conf, bots_list
    try:
        file_cfg = open('settings.cfg', 'r+')
        settings_conf = [line.strip() for line in file_cfg]
        for i in range(3, len(settings_conf)):
            r = requests.get(f'{vk_api}/account.getProfileInfo?{vk_cfg}{settings_conf[i]}').json()
            bots_list.append({'token': settings_conf[i], 'name': f"{r['response']['first_name']} {r['response']['last_name']}", 'target': settings_conf[0], 'last_id': '0'})
            print(f"Bot {i-2}: {r['response']['first_name']} {r['response']['last_name']}")
        print(f'Target link: {settings_conf[0]}')
    except FileNotFoundError:
        print('Settings file not found, please run install')
    except Exception as excp:
        print(f'Error while get settings: {excp}')
        # print(f"Bot {i}: {r['error']['error_msg']}")

get_settings()


def get_type(target):
    try:
        target = target[target.index('vk.com/'):][7:]
        vk_resp = requests.get(f'{vk_api}/utils.resolveScreenName?screen_name={target}{vk_cfg}').json()
        _type = vk_resp['response']['type']
        _id = vk_resp['response']['object_id']
        return [_type, _id]
    except ValueError:
        print('Bad target link')
    except IndexError:
        print('Bots not found')
    except Exception as excp:
        print(f'Error while get link type: {excp}')


def get_friends(_id):
    try:
        print('Get user friends...')
        ulist = requests.get(f'{vk_api}/friends.get?order=name&user_id={_id}{vk_cfg}').json()
        return ulist['response']['items']
    except Exception as excp:
        print(f'Error while get friends: {excp}')


def get_members(_id):
    try:
        print('Get group members...')
        ulist = requests.get(f'{vk_api}/groups.getMembers?count=0&group_id={_id}{vk_cfg}').json()
        members_count = ulist['response']['count']
        if (members_count % 1000) > 0:
            reqs_nums = (members_count / 1000) + 1
        else:
            reqs_nums = members_count / 1000
        target_ulist = []
        for i in range(0, int(reqs_nums)):
            ulist = requests.get(f'{vk_api}/groups.getMembers?offset={i*1000}&group_id={_id}{vk_cfg}').json()
            target_ulist += (ulist['response']['items'])
            time.sleep(0.1)
        return target_ulist
    except Exception as excp:
        print(f'Error while get members: {excp}')


# get_type('https://vk.com/worket')


def get_used_ids(token):
    data = sqlite3.connect('data.db')
    c = data.cursor()
    t = (token,)
    used_ids = []
    for row in c.execute("select last_id from requests where token=?", t):
        used_ids.append(row[0])
    data.commit()
    data.close()
    return used_ids


def get_target_ids(token, ids):
    target_ids = ids
    for i in ids:
        for j in get_used_ids(token):
            if i == j:
                target_ids.remove(i)
    return target_ids


def get_user(_id):
    try:
        vk_req = requests.get(f'{vk_api}/users.get?user_ids={_id}&fields=last_seen{vk_cfg}').json()
        last_seen = int(vk_req['response'][0]['last_seen']['time'])
        if 'deactivated' not in vk_req['response']:
            if int(settings_conf[1]) == 0 or last_seen > time.time() - int(settings_conf[1]) * 86400:
                return f"{vk_req['response'][0]['first_name']} {vk_req['response'][0]['last_name']}"
        else:
            print('User deleted of inactive > of limit')
            return None
    except:
        print('Error while get user')


def send_request(ids_list):
    for _id in ids_list:
        for bot in range(len(bots_list)):
            data = sqlite3.connect('data.db')
            cur = data.cursor()
            cur.execute("select last_id from requests where token=? and destination=?", (bots_list[bot]["token"], settings_conf[0]))
            last_added_id = cur.fetchone()[0]
            print(last_added_id)
            if last_added_id is None:
                cur.execute("insert into requests (token, destination, last_id) values (?, ?, ?)", (bots_list[bot]["token"], settings_conf[0], 0))
            data.commit()
            data.close()
            target_uname = get_user(_id)
            if target_uname and int(_id) > int(last_added_id):
                req = f'{vk_api}/friends.add?user_id={_id}{vk_cfg}{bots_list[bot]["token"]}'
                vk_req = requests.get(req).json()
                print(f'{bots_list[bot]["name"]}: adding to friends {target_uname}')
                if 'error' in vk_req:
                    if vk_req['error']['error_code'] == 14:
                        print('Captcha needed, request to anti-captcha.com...')
                        urlretrieve(vk_req['error']['captcha_img'], 'captcha.jpg')
                        captcha_key = AntiGate('d92e4ba5cd6971511b017cc0bd70abaa', 'captcha.jpg')
                        vk_req = requests.get(f"{req}&captcha_sid={vk_req['error']['captcha_sid']}&captcha_key={captcha_key}").json()
                    else:
                        print('Reached limit of requests')
                if 'response' in vk_req:
                    if vk_req['response'] == 1:
                        bots_list[bot]['last_id'] = _id
                        data = sqlite3.connect('data.db')
                        cur = data.cursor()
                        cur.execute("update requests set last_id=? where token=? and destination=?", (_id, bots_list[bot]["token"], settings_conf[0]))
                        data.commit()
                        data.close()
                        print('OK')
                    elif vk_req['response'] == 4:
                        print('Double request')
                print(f'{vk_req}')
        time.sleep(10)

for i in range(len(bots_list)):
    # try:
    #     type_id = get_type(settings_conf[0])
    #     if type_id[0] == 'user':
    #         list_ids = get_friends(type_id[1])
    #     elif type_id[0] == 'group':
    #         list_ids = get_members(type_id[1])
    #     send_request(tokens_list[i], get_target_ids(settings_conf[1], list_ids))
    # except TypeError:
    #     # print('Error while get target link type')
    #     print('Error')
    type_id = get_type(settings_conf[0])
    if type_id[0] == 'user':
        list_ids = get_friends(type_id[1])
    elif type_id[0] == 'group':
        list_ids = get_members(type_id[1])
    send_request(get_target_ids(bots_list[i]['token'], list_ids))
