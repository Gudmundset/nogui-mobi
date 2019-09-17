# mobi-stations.py
Sometimes, you just don't want a GUI. I made this to email myself every morning when I get to Waterfront to let me know if there are any bikes at Cordova & Granville.

REPL: https://repl.it/repls/SnoopySoupyFtpclient

Get all stations on Granville with minimum 10 bikes:

runner@repl.it:~$ python main.py -m 10 Granville

{'name': '0015 Granville & Georgia', 'coordinates': '49.282409, -123.118541', 'total_slots': 20, 'free_slots': 8, 'avl_bikes': 12, 'operative': True, 'style': ''}
{'name': '0063 Robson & Granville', 'coordinates': '49.281506,  -123.120101', 'total_slots': 32, 'free_slots': 17, 'avl_bikes': 15, 'operative': True, 'style': ''}

# mobi-ride-stats.py
The website makes no assumptions so I did a few calculations. I was interested in bagging the data and finding out which series was the fastest. Based on the data, 15**, 16** and 03** are the best ones for my riding style.

mobi-ride-stats REPL: https://repl.it/@PhilipLarson/CompetitiveEverlastingSoftwareagent

runner@repl.it:~$ python mobi-ride-stats.py

number of rides analyzed: 499

fastest rides:
1662: 1.04 km/h
0482: 0.93 km/h
1545: 0.90 km/h
0045: 0.88 km/h
0114: 0.87 km/h
1029: 0.82 km/h
0676: 0.81 km/h
0547: 0.76 km/h
1206: 0.76 km/h
0590: 0.75 km/h
0797: 0.75 km/h

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
[('20**', 0.0625), ('16**', 0.08333333333333333), ('19**', 0.09090909090909091), ('12**', 0.3333333333333333), ('10**', 0.34615384615384615), ('13**', 0.36363636363636365), ('08**', 0.38461538461538464), ('04**', 0.4), ('03**', 0.40625), ('06**', 0.4090909090909091), ('11**', 0.41935483870967744), ('02**', 0.42857142857142855), ('01**', 0.42857142857142855), ('09**', 0.43333333333333335), ('07**', 0.4444444444444444), ('14**', 0.4444444444444444), ('05**', 0.45454545454545453), ('00**', 0.45714285714285713), ('15**', 0.46153846153846156)]

fastest numeral range:
[('15**', 0.46153846153846156), ('00**', 0.45714285714285713), ('05**', 0.45454545454545453), ('07**', 0.4444444444444444), ('14**', 0.4444444444444444), ('09**', 0.43333333333333335), ('02**', 0.42857142857142855), ('01**', 0.42857142857142855), ('11**', 0.41935483870967744), ('06**', 0.4090909090909091), ('03**', 0.40625), ('04**', 0.4), ('08**', 0.38461538461538464), ('13**', 0.36363636363636365), ('10**', 0.34615384615384615), ('12**', 0.3333333333333333),('19**', 0.09090909090909091), ('16**', 0.08333333333333333), ('20**', 0.0625)]

series numbers considered:
['00**', '01**', '02**', '03**', '04**', '05**', '06**', '07**', '08**', '09**', '10**', '11**', '12**', '13**', '14**', '15**', '16**', '17**', '18**', '19**', '20**', '21**']
