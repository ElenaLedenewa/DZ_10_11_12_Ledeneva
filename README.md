home_work_10

#Назначение проекта
    Проект реализует функционал по работе над виджетом
банковских операций клиента.
Реализует подготовку информации по банковской карте 
или счёту клиента. Карта и счёт представляются в виде
маски.

# Использование
    Приложение работает со строковым представлением
    вида банковской карты или счёта, например:
    Visa Platinum 7000 7922 8960 6361,
    или Maestro 7000 7922 8960 6361,
    или Счет 73654108430135874305.
    Возвращает исходную строку с замаскированным
     номером карты/счета.
1. Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX .
    Т. е. видны первые 6 цифр и последние 4, номер 
    разбит по блокам по 4 цифры, разделенным 
    пробелами.
    Пример работы функции, возвращающей маску карты
        7000792289606361     # входной аргумент
        7000 79** **** 6361  # выход функции
2. Номер счета замаскирован и отображается в формате
    **XXXX. Т. е. видны только последние 4 цифры.
    Пример работы функции, возвращающей маску счета
      73654108430135874305  # входной аргумент
      **4305  # выход функции

#Документация:  
    в работе

#Лицензия: нет
