@echo off
title [Install - VK Add Friends Bot]
pip install -r requirements.txt
python -c "cfg = open('settings.cfg', 'w'); cfg.write(input('Enter Target Link:\n') + '\n'); cfg.close(); import sqlite3; data = sqlite3.connect('data.db'); c = data.cursor();c.execute('CREATE TABLE requests (token TEXT, destination TEXT, id TEXT)');data.commit;data.close()"
echo.
pause