from widget import get_data, mask_account_card  # type: ignore
from processing import sort_by_date, filter_by_state  # type: ignore


list_id = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:34.419441'}]

print(mask_account_card("Visa Platinum 7000 7922 8960 6361"))

print(get_data("2018-07-11T02:26:18.671407"))
print(sort_by_date(list_id))
print(filter_by_state(list_id, state_id='CANCELED'))
