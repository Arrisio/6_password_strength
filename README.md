# Определение сложности пароля

Программа вычисляет сложность пароля. Ввод пароля для анализа осуществляется через командную строку.
Программа выдаёт ему оценку от 1 до 10. 1 – очень слабый пароль, 10 – очень крутой.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5.
При запуске с ключем `-b` можно указать файл со списком распространенных паролей, который можно взять , например, [отсюда](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials)

Запуск на Linux:

```bash

$ python password_strength.py -b passwords_blacklist.txt
Enter the personal data that will be used to verify the password: Vasya Pupkin 1990
Enter password:
Password strength:  4
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)

