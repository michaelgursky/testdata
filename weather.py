import datetime
import pandas as pd
import json

def csv_append(fn, ts, value):
  dt = datetime.datetime.fromtimestamp(ts)
  df = pd.DataFrame({"timestamp": [dt], "value": [value]})
  df.to_csv(fn, mode='a', index=False, header=False, date_format="%Y-%m-%dT%H:%M:%S")

if __name__ == "__main__":
  configName = "weather-06089.json"
  f = open(configName, 'r')
  data = json.load(f)
  f.close()

  ts = data["dt"]
  temp = data["main"]["temp"]
  humidity = data["main"]["humidity"]

  csv_append("weather-temp.csv", ts, temp)
  csv_append("weather-humidity.csv", ts, humidity)
