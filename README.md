# mobi-stations.py
Sometimes, you just don't want a GUI. I made this to email myself every morning when I get to Waterfront to let me know if there are any bikes at Cordova & Granville.

mobi-stations REPL: https://repl.it/repls/SnoopySoupyFtpclient

Get all stations on Granville with minimum 10 bikes:

runner@repl.it:~$ python main.py -m 10 Granville

{'name': '0015 Granville & Georgia', 'coordinates': '49.282409, -123.118541', 'total_slots': 20, 'free_slots': 8, 'avl_bikes': 12, 'operative': True, 'style': ''}\
{'name': '0063 Robson & Granville', 'coordinates': '49.281506,  -123.120101', 'total_slots': 32, 'free_slots': 17, 'avl_bikes': 15, 'operative': True, 'style': ''}

# mobi-ride-stats.py
The website makes no assumptions so I did a few calculations. I was interested in bagging the data and finding out which series was the fastest. Based on the data, 15**, 16** and 03** are the best ones for my riding style.

mobi-ride-stats REPL: https://repl.it/@PhilipLarson/CompetitiveEverlastingSoftwareagent

runner@repl.it:~$ python mobi-ride-stats.py

number of rides analyzed: 499

fastest rides:
1662: 30.00 km/h   (30-08-2018 10h13m26 - 30-08-2018 10h24m40) - 5.583kms
0656: 19.01 km/h   (19-06-2018 10h22m34 - 19-06-2018 10h31m39) - 2.852kms
1551: 18.51 km/h   (31-07-2018 09h54m47 - 31-07-2018 10h04m07) - 2.858kms
0676: 18.07 km/h   (15-08-2018 09h58m06 - 15-08-2018 10h07m39) - 2.856kms
1943: 18.01 km/h   (02-08-2018 09h44m08 - 02-08-2018 09h53m46) - 2.871kms
1020: 17.87 km/h   (29-05-2018 10h01m33 - 29-05-2018 10h11m07) - 2.824kms
0606: 17.85 km/h   (09-05-2018 09h14m41 - 09-05-2018 09h24m19) - 2.846kms
1471: 17.72 km/h   (14-08-2018 09h19m55 - 14-08-2018 09h29m43) - 2.869kms
0267: 17.50 km/h   (21-06-2018 10h08m23 - 21-06-2018 10h18m12) - 2.844kms
1262: 17.47 km/h   (01-08-2018 09h43m52 - 01-08-2018 09h53m49) - 2.877kms
0079: 17.35 km/h   (08-08-2018 09h55m42 - 08-08-2018 10h05m40) - 2.862kms

most common individual bikes:
1: ('1273', 4))
2: ('0377', 4))
3: ('0353', 4))
4: ('1622', 3))
5: ('0925', 3))
6: ('1020', 3))
7: ('0336', 3))
8: ('0322', 3))
9: ('1210', 3))
10: ('0509', 3))

most common numeral range:
1: ('04**', 45))
2: ('12**', 39))
3: ('00**', 35))
4: ('03**', 32))
5: ('11**', 31))
6: ('09**', 30))
7: ('02**', 28))
8: ('14**', 27))
9: ('07**', 27))
10: ('10**', 26))

slowest numeral range (series, avg speed km/h:
[('20**', 8.3125), ('18**', 8.5), ('21**', 9.4), ('17**', 10.0), ('13**', 10.272727272727273), ('12**', 10.897435897435898), ('16**', 10.916666666666666), ('19**', 11.181818181818182), ('10**', 11.5), ('15**', 11.76923076923077), ('04**', 11.8), ('05**', 11.863636363636363), ('03**', 12.03125), ('00**', 12.257142857142858), ('14**', 12.333333333333334), ('09**', 12.4),('08**', 12.423076923076923), ('01**', 12.571428571428571), ('02**', 12.607142857142858), ('11**', 12.67741935483871), ('07**', 12.88888888888889), ('06**', 13.090909090909092)]

fastest numeral range:
[('06**', 13.090909090909092), ('07**', 12.88888888888889), ('11**', 12.67741935483871), ('02**', 12.607142857142858), ('01**', 12.571428571428571), ('08**', 12.423076923076923), ('09**', 12.4), ('14**', 12.333333333333334), ('00**', 12.257142857142858), ('03**', 12.03125), ('05**', 11.863636363636363), ('04**', 11.8), ('15**', 11.76923076923077), ('10**', 11.5), ('19**', 11.181818181818182), ('16**', 10.916666666666666), ('12**', 10.897435897435898), ('13**',10.272727272727273), ('17**', 10.0), ('21**', 9.4), ('18**', 8.5), ('20**', 8.3125)]

series numbers considered:
['00**', '01**', '02**', '03**', '04**', '05**', '06**', '07**', '08**', '09**', '10**', '11**', '12**', '13**', '14**', '15**', '16**', '17**', '18**', '19**', '20**', '21**']
