from collections import Counter

def scrape_ridedata(data):
  rides = []
  for no,line in enumerate(data):
    if no == 0:
      header_data = line.split('\t')
    line_list = line.split('\t')
    rides.append(dict(zip(header_data, line_list)))
  return rides

def main():
  filepath = "phil_ridedata"
  with open(filepath) as f:
    data = f.readlines()

  rides = scrape_ridedata(data)

  c = Counter()
  for r in rides:
    bike = r['BIKE']
    print(bike)
    c[bike] += 1

  print('most common bike', c.most_common(10))

if __name__ == "__main__":
  main()
