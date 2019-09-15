# nogui-mobi
Sometimes, you just don't want a GUI. I made this to email myself every morning when I get to Waterfront to let me know if there are any bikes at Cordova & Granville.

REPL: https://repl.it/repls/SnoopySoupyFtpclient
mobi-ride-stats REPL: https://repl.it/@PhilipLarson/CompetitiveEverlastingSoftwareagent

Get all stations on Granville with minimum 10 bikes:

runner@repl.it:~$ python main.py -m 10 Granville

{'name': '0015 Granville & Georgia', 'coordinates': '49.282409, -123.118541', 'total_slots': 20, 'free_slots': 8, 'avl_bikes': 12, 'operative': True, 'style': ''}
{'name': '0063 Robson & Granville', 'coordinates': '49.281506,  -123.120101', 'total_slots': 32, 'free_slots': 17, 'avl_bikes': 15, 'operative': True, 'style': ''}


most common bike [('1273', 4), ('0377', 4), ('0353', 4), ('1622', 3), ('0925', 3), ('1020', 3), ('0336', 3), ('0322', 3), ('1210', 3), ('0509', 3)]
