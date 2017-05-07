Установка Python для Windows:
---
* Скачать  и распаковать архив с ботом по ссылке:
https://github.com/Bionic-Leha/vkfriendspam/archive/master.zip
* Скачать и запустить установочный файл:
https://www.python.org/ftp/python/3.6.1/python-3.6.1.exe
* Отметить 'Add Python 3.6 to PATH'
* Нажать 'Install Now'
* Запустить из папки с ботом 'install.bat'

Настройки бота (текстовый файл settings.cfg):
---
* Самая первая строка отвечает за текущую "цель" - ссылка на группу или человека
* В последующие строки помещаются токены аккаунтов, которые будут отправлять заявки

Как получить токен аккаунта:
---
* Шаблон ссылки: https://oauth.vk.com/token?grant_type=password&scope=friends&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username=USER&password=PASS
* Заменить в ссылке USER на телефон/email ВК аккаунта
* Заменить PASS на пароль ВК аккаунта
* Перейти по измененной ссылке
* Получить ответ, если ваш ответ, схожий на
>{"access_token":"4795krd78ag1c369db1ea288743a110d8571379405435f0160c26493988c64d88c02fe8c887bcd53a9ac7","expires_in":0,"user_id":374996700}
* Скопировать набор символов, расположенный в кавычках, после "access_token", не включая сами кавычки
* Пример токена
>4795krd78ag1c369db1ea288743a110d8571379405435f0160c26493988c64d88c02fe8c887bcd53a9ac7

Дополнительная информация:
---
* Желательно, что бы токен был получен с того же IP адреса, где будет работать сам бот.
* Пример файла settings.cfg:
>https://vk.com/worket
>4795krd78ag1c369db1ea288743a110d8571379405435f0160c26493988c64d88c02fe8c887bcd53a9ac7
>43a110d8571379405435f0160c4795krd78ag1c369db1ea288726493988c64d88c02fe8c887bcd53a9ac7
* Запуск бота - 'run.bat' (windows)