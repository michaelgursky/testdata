import datetime
import pandas as pd
from xml.dom.minidom import parse, parseString

def csv_append(fn, dt, value):
  df = pd.DataFrame({"timestamp": [dt], "value": [value]})
  df.to_csv(fn, mode='a', index=False, header=False, date_format="%Y-%m-%dT%H:%M:%S")

if __name__ == "__main__":
  readingFile = "weather-06089.xml"
  tree = parse(readingFile).childNodes[0].childNodes
  temperature = [n for n in tree if n.nodeName == "temperature"][0].getAttribute("value")
  humidity = [n for n in tree if n.nodeName == "humidity"][0].getAttribute("value")
  p = [n for n in tree if n.nodeName == "precipitation"][0]
  precipitation = 0 if (p.getAttribute("mode") == "no") else p.getAttribute("value")
  dt = [n for n in tree if n.nodeName == "lastupdate"][0].getAttribute("value")

  csv_append("weather-temperature.csv", dt, temperature)
  csv_append("weather-humidity.csv", dt, humidity)
  csv_append("weather-precipitation.csv", dt, precipitation)
