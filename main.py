from yahoo_historical import Fetcher
import requests

identifiers = []
with open("symbols.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        identifiers.append(line.split('\n')[0])

path = './data'
startDate = [1994,1,1]
endDate = [2019,5,19]

for s in identifiers:
    fetcher = Fetcher(s, startDate, endDate)
    fetcher.saveHistoricalData(events='history', rootPath=path)