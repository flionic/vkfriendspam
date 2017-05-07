@echo off
title [Install - VK Add Friends Bot]
pip install -r requirements.txt
python -c "cfg = open('settings.cfg', 'w'); cfg.write(input('Enter Target Link:\n')); cfg.close()"
echo.
pause