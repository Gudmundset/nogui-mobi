# nogui-mobi
Sometimes, you just don't want a GUI

REPL: https://repl.it/repls/SnoopySoupyFtpclient

Get all stations on Granville with minimum 10 bikes:

runner@repl.it:~$ python main.py -m 10 Granville
{'name': '0015 Granville & Georgia', 'coordinates': '49.282409, -123.118541', 'total_slots': 20, 'free_slots': 8, 'avl_bikes': 12, 'operative': True, 'style': ''}
{'name': '0063 Robson & Granville', 'coordinates': '49.281506,  -123.120101', 'total_slots': 32, 'free_slots': 17, 'avl_bikes': 15, 'operative': True, 'style': ''}
