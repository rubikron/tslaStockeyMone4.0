from  weekDataPercentDiff import getData
from  weekDataPercentDiff import percentDif
from yahoo_finance_api2 import share
from datetime import datetime
import pandas as pd


weekPerDif = percentDif(getData(),'open')
tslaDf = pd.read_csv("tslaDataset.csv")
tslaDf = tslaDf.drop(['unnamed'], axis = 1)

dateList = []
dfPriceList = []
for x in range(len(tslaDf)):
	dateList.append(tslaDf["timestamp"][x])
	dfPriceList.append(tslaDf["open"][x])

dfDataset = {"timestamp":dateList,"open":dfPriceList}

dfOpenPerDif = percentDif(dfDataset,"open")


weekDfPercDif = []
for y in range(len(dfOpenPerDif)-3):

	weekDfPercDif.append([(weekPerDif[0][0] - dfOpenPerDif[y][0]),
	(weekPerDif[0][0] - dfOpenPerDif[y+1][0]),
	(weekPerDif[0][0] - dfOpenPerDif[y+2][0]),
	(weekPerDif[0][0] - dfOpenPerDif[y+3][0]),
	dfOpenPerDif[y][1],dfOpenPerDif[y+3][2]])
weekDfPercDif = weekDfPercDif[:-1]
currentWeekPercs = percentDif(getData(),"open")

weekCurrentPercDifList = []

for b in weekDfPercDif:
	listAppended = []
	for a in range(4):
		listAppended.append(currentWeekPercs[a][0] - b[a])
	listAppended.append(b[-2])
	listAppended.append(b[-1])
	weekCurrentPercDifList.append(listAppended)
weekdCurrentPercDifListNoAbs = weekCurrentPercDifList
for s in weekCurrentPercDifList:
	for t in range(4):
		s[t] = abs(s[t])
# print(weekCurrentPercDifList)
weekCurrentPercValList = []
for d in range(len(weekCurrentPercDifList)):
	weekCurrentPercDifList[d].append((weekCurrentPercDifList[d][0] + weekCurrentPercDifList[d][1] + weekCurrentPercDifList[d][2] + weekCurrentPercDifList[d][3])/4)
	weekCurrentPercValList.append([weekCurrentPercDifList[d][-1]])

weekCurrentPercValList.sort()
del weekCurrentPercValList[8:-1]
for e in range(len(weekCurrentPercValList)):
	for f in range(len(weekCurrentPercDifList)):
		if weekCurrentPercValList[e][0] == weekCurrentPercDifList[f][-1]:
			weekCurrentPercValList[e].append(weekCurrentPercDifList[f][-3])
			weekCurrentPercValList[e].append(weekCurrentPercDifList[f][-2])
			weekCurrentPercValList[e].append(weekCurrentPercDifList[f][0])
			weekCurrentPercValList[e].append(weekCurrentPercDifList[f][1])
			weekCurrentPercValList[e].append(weekCurrentPercDifList[f][2])
			weekCurrentPercValList[e].append(weekCurrentPercDifList[f][3])

print(weekCurrentPercValList)
# right now, first value of weekCurrentPercValList is the average difference of the percent change, 
# second value is start date, third value is end date
# fourth through eitgth values are the price changes of the 5 days

# next you need to use the current dates and find the future percent changes, apply it for today's price, and tell if I should invest in Tesla stock  



def findPriceFromDate(date, category,indexIncrement = 0):
	return tslaDf[category][list(tslaDf["timestamp"]).index(date) + indexIncrement]


