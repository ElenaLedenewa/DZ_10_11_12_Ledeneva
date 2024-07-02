from typing import Any


def filter_by_state(transactions: list[dict[str, Any]], state_transac: str = 'EXECUTED') -> list[dict[str, Any]]:
    """ Фильтрует список транзакций по заданному состоянию.

        Принимает на вход список словарей и значение для ключа state
        (опциональный параметр со значением по умолчанию EXECUTED)
        и возвращает новый список, содержащий только те словари,
        у которых ключ state содержит переданное в функцию значение.

        :param transactions: Список транзакций.
         :param state_transac: Состояние для фильтрации (по умолчанию 'EXECUTED').
         :return: Отфильтрованный список транзакций.

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

    transactions_new = []

    for transaction in transactions:
        if transaction['state'] == state_transac:
            transactions_new.append(transaction)

    return transactions_new


def sort_by_date(transactions: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """ Сортировка транзакций по времени выполнения.

        Функция принимает на вход список транзакций и возвращает новый список,
       в котором транзакции отсортированы по убыванию даты (ключ date).
       Второй необязательный аргумент reverse  задает порядок сортировки по методу
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

    sorted_transactions = sorted(transactions, key=lambda x: x['date'])

    return sorted_transactions
