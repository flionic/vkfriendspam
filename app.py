try:
    settings_conf = open('text.txt', 'r')
except FileNotFoundError:
    print('File not found')
