Установка бота для Windows:
---
* Скачать  и распаковать архив с ботом по ссылке:
https://github.com/Bionic-Leha/vkfriendspam/archive/release.zip
* Скачать и запустить установочный файл Python:
https://www.python.org/ftp/python/3.6.1/python-3.6.1.exe
* Отметить 'Add Python 3.6 to PATH'
* Нажать 'Install Now'
* Запустить из папки с ботом 'install.bat'
* Вставить ссылку на группу/человека
* Указать период неактивности страницы, в днях (0 - выключить)
* Вставить ключ из сервиса https://anti-captcha.com/clients/settings/apisetup
>Повторный запуск 'install.bat приведет к полному сбросу настроек'

Настройки бота (текстовый файл settings.cfg):
---
* Первая строка задает текущую цель (ссылка на группу или человека)
* Вторая строка содержит ключ сервиса https://anti-captcha.com/
* Последующие строки содержат токены аккаунтов, которые будут отправлять заявки

Как добавить аккаунт бота:
---
* Запустить 'add_bot.bat'
* Ввести логин или email
* Ввести пароль
* Ответ содержит в себе имя+фамилию бота, либо ошибку

>Запуск бота - 'run.bat' (windows)