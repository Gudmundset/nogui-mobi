from collections import Counter
import re
from operator import itemgetter

def scrape_ridedata(data):
  '''
  Function: return rides + header data from ridedata file
  '''
  rides = []
  for no,line in enumerate(data):
    if no == 0:
      #should only run the first time
      header_data = line.split('\t')
      header_data = [h.strip() for h in header_data]
    line_list = line.split('\t')
    line_list = [l.strip() for l in line_list]
    rides.append(dict(zip(header_data, line_list)))
  return rides, header_data

def get_hour(duration):
  '''
  Function: return how many seconds long the ride was
  '''
  return sum(int(x) * 60 ** i for i,x in enumerate(reversed(duration))) / 3600

def get_km(distance):
  '''
  Function: return how far in meters
  '''
  if 'kms' in distance:
    return float(re.search(r'[0-9\.]+', distance)[0])
  else:
    return float(re.search(r'[0-9\.]+', distance)[0])*.001

def ride_stats(rides, headers):
  '''
  Function: Find stats on ride objects
  '''
  mostcommon = Counter()
  commonseries = Counter()
  fastestseries = Counter()
  ride_list = []
  for _,ride in enumerate(rides):
    if _ == 0: #ignore headers
        continue
    # fastest rides ---------------------------------
    howie_long = re.findall(r'\d+', ride['DURATION'])
    howie_long = get_hour(howie_long)
    how_far = get_km(ride['DISTANCE COVERED'])
    how_fast = howie_long * how_far
    ride['HOW_FAST'] = how_fast
    ride_list.append(ride)
    
    # most common bikes ------------------------
    for h in headers:
      mostcommon[ride[h]]
    bike = ride['BIKE']
    mostcommon[bike] += 1

    # fastest series ------------------------
    fastestseries[bike[:2] +'**'] += how_fast

    # common series ------------------
    commonseries[bike[:2] +'**'] += 1

    

  print('\nnumber of rides analyzed: {0}'.format(len(ride_list)-1))
  
  print('\nfastest rides:') 
  ride_list = sorted(ride_list, key=itemgetter('HOW_FAST'))
  for _,ride in enumerate(reversed(ride_list)):
    if _ > 10:
        break
    print('{0}: {1:.2f} km/h'.format(ride['BIKE'], ride['HOW_FAST']))

  print('\nmost common individual bikes:') 
  for n,b in enumerate(mostcommon.most_common(10)):
    print(f'{n+1}: {b})')
  
  print('\nmost common numeral range:') 
  for n,b in enumerate(commonseries.most_common(10)):
    print(f'{n+1}: {b})')

  
  fastestrange = []
  for b in fastestseries.most_common():
    if int(b[1]) > 0:
      result = int(b[1]) / commonseries[b[0]]
      fastestrange.append((b[0], result))
  print('\nslowest numeral range (series, avg speed km/h:')
  print(sorted(fastestrange, key=itemgetter(1)))
  print('\nfastest numeral range:')
  print(sorted(fastestrange, key=itemgetter(1), reverse=True))
  print('\nseries numbers considered:')
  print(sorted([f for f in commonseries]))


def main():
  '''
  Xhu Li, do The Thing
  '''
  filepath = "phil_ridedata"
  try:
    with open(filepath) as f:
      data = f.readlines()
  except IOError as e:
    print(e)

  if data:
    rides, headers = scrape_ridedata(data)
    ride_stats(rides, headers)

if __name__ == "__main__":
  main()
