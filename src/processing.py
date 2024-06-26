from typing import Any


def filter_by_state(list_id: Any, state_id: str = 'EXECUTED') -> list:
    """ принимает на вход список словарей и значение для ключа state
        (опциональный параметр со значением по умолчанию EXECUTED)
        и возвращает новый список, содержащий только те словари,
        у которых ключ state содержит переданное в функцию значение.
        Вход функции [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

        Выход функции со статусом по умолчанию EXECUTED
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

        Выход функции, если вторым аргументом передано 'CANCELED'
        [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

        (list_id: Any, state_id: str = 'EXECUTED') -> None
        """

    list_id_new = []

    for id_operation in list_id:
        if id_operation['state'] == state_id:
            list_id_new.append(id_operation)

    return list_id_new


def sort_by_date(list_id: Any, reverse: bool = True) -> list:
    """ принимает на вход список словарей и возвращает новый список,
       в котором исходные словари отсортированы по убыванию даты (ключ date).
       Функция принимает два аргумента, второй необязательный задает порядок сортировки по методу
       (убывание, возрастание).
       Вход функции
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

        Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

        dict_id: {items}, sorting_order: bool = True) -> list
        """

    sorted_list_id = sorted(list_id, key=lambda x: x['date'])

    return sorted_list_id
