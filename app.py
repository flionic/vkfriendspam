main_token = ''
vk_api = 'https://api.vk.com/method/'
vk_cfg = '&access_token=' + main_token + '&v=5.64'
settings_conf = {}
target_ulist = {}


def get_settings():
    global settings_conf
    try:
        file_cfg = open('settings.cfg', 'r')
        settings_conf = [line.strip() for line in file_cfg]
        print(settings_conf)
    except FileNotFoundError:
        print('File not found, creating it')
        open('settings.cfg', 'w')
    except Exception as excp:
        print(excp)
get_settings()
