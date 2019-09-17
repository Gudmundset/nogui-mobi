import requests
import argparse

def get_stations(api, str_arg, min_bikes):

  for i in api.json()['result']:
      if str_arg in i['name']:
        if i['operative'] == True:
          if int(i['avl_bikes']) > min_bikes:
            print({k:v for k,v in i.items()})

def get_options():
  default_api = 'http://vancouver-ca.smoove.pro/api-public/stations'
  default_station = "Cordova & Granville"
  default_minbikes = 1

  parser = argparse.ArgumentParser()
  parser.add_argument("station", type=str,
                    help=f"display all public station info", nargs='*', default=default_station)
  parser.add_argument("-a", "--api", help=f"specify API url. default is {default_api}",
                    default=default_api, required=False)
  parser.add_argument("-m", "--minbikes", help=f"specify API url. default is {default_minbikes}",
                    default=default_minbikes, required=False, type=int)                  
                    
  args = parser.parse_args()
  return args

def main():
    options = get_options()
    r = requests.get(options.api)
    if options.station:
      for station in options.station:
        get_stations(r, station, options.minbikes)
    else:
        get_stations(r, station, options.minbikes)


if __name__ == "__main__":
    main()
