@echo off
title [Install - VK Add Friends Bot]
pip install -r requirements.txt
python -c "open('settings.cfg', 'w')"
echo.
pause