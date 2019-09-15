from collections import Counter

def scrape_ridedata(data):
  '''
  Function: return rides + header data from ridedata file
  '''
  rides = []
  for no,line in enumerate(data):
    if no == 0:
      header_data = line.split('\t')
    line_list = line.split('\t')
    rides.append(dict(zip(header_data, line_list)))
  return rides, header_data

def ride_stats(rides, headers):
  '''
  Function: Find stats on ride objects
  '''
  c = Counter()
  for r in rides:
    bike = r['BIKE']
    c[bike] += 1

  print('most common bikes:') 
  for n,b in enumerate(c.most_common(10)):
    print(f'{n+1}: {b})')


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


