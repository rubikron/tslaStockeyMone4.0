from  weekDataPercentDiff import getData
from  weekDataPercentDiff import percentDif
from  weekDataPercentDiff import percentDifSimple
from yahoo_finance_api2 import share
from datetime import datetime
import pandas as pd


weekPerDif = percentDif(getData(6),"close")
tslaDf = pd.read_csv("tslaDataset.csv")
tslaDf = tslaDf.drop(['unnamed'], axis = 1)

dateList = []
dfPriceList = []
for x in range(len(tslaDf)):
	dateList.append(tslaDf["timestamp"][x])
	dfPriceList.append(tslaDf["close"][x])

dfDataset = {"timestamp":dateList,"close":dfPriceList}

dfOpenPerDif = percentDif(dfDataset,"close")


weekDfPercDif = []
for y in range(len(dfOpenPerDif)-3):

	weekDfPercDif.append([(weekPerDif[0][0] - dfOpenPerDif[y][0]),
	(weekPerDif[0][0] - dfOpenPerDif[y+1][0]),
	(weekPerDif[0][0] - dfOpenPerDif[y+2][0]),
	(weekPerDif[0][0] - dfOpenPerDif[y+3][0]),
	dfOpenPerDif[y][1],dfOpenPerDif[y+3][2]])
weekDfPercDif = weekDfPercDif[:-1]
currentWeekPercs = weekPerDif
# print(currentWeekPercs)
weekCurrentPercDifList = []

for b in weekDfPercDif:
	listAppended = []
	for a in range(4):
		listAppended.append(currentWeekPercs[a][0] - b[a])
	listAppended.append(b[-2])
	listAppended.append(b[-1])
	weekCurrentPercDifList.append(listAppended)



weekCurrentPercValList = []
for d in range(len(weekCurrentPercDifList)):
	weekCurrentPercDifList[d].append((abs(weekCurrentPercDifList[d][0]) + abs(weekCurrentPercDifList[d][1]) + abs(weekCurrentPercDifList[d][2]) + abs(weekCurrentPercDifList[d][3]))/4)
	weekCurrentPercValList.append([weekCurrentPercDifList[d][-1]])
for s in weekCurrentPercDifList:
	s[-1] = abs(s[-1])
	


weekCurrentPercValList.sort()

for e in range(len(weekCurrentPercValList)):
	for f in range(len(weekCurrentPercDifList)):
		if weekCurrentPercValList[e][0] == weekCurrentPercDifList[f][-1]:
			weekCurrentPercValList[e].append(weekCurrentPercDifList[f][-3])
			weekCurrentPercValList[e].append(weekCurrentPercDifList[f][-2])
			weekCurrentPercValList[e].append(weekCurrentPercDifList[f][0])
			weekCurrentPercValList[e].append(weekCurrentPercDifList[f][1])
			weekCurrentPercValList[e].append(weekCurrentPercDifList[f][2])
			weekCurrentPercValList[e].append(weekCurrentPercDifList[f][3])
# print(weekCurrentPercValList)

# right now, first value of weekCurrentPercValList is the average difference of the percent change, 
# second value is start date, third value is end date
# fourth through eitgth values are the price changes of the 5 days

# next you need to use the current dates and find the future percent changes, apply it for today's price, and tell if I should invest in Tesla stock  


priceChangeDiffAvgList = []
for h in range(len(weekCurrentPercDifList)):
	priceChangeDiffAvgList.append([weekCurrentPercDifList[h][-1]])

priceChangeDiffAvgList.sort()
priceChangeDiffAvgList = priceChangeDiffAvgList[:14:]

for l in priceChangeDiffAvgList:
	for m in weekCurrentPercDifList:
		if m[-1] == l[0]:
			l.append(m[-3])
			l.append(m[-2])


def findPriceFromDate(date, category,indexIncrement = 0):
	return tslaDf[category][list(tslaDf["timestamp"]).index(date) + indexIncrement]


futurePercDiff = {}


for u in priceChangeDiffAvgList:
	futurePercDiff[str(u[-1])] = [findPriceFromDate(str(u[-1]),"close"),findPriceFromDate(str(u[-1]),"close",1),findPriceFromDate(str(u[-1]),"close",2),findPriceFromDate(str(u[-1]),"close",3),findPriceFromDate(str(u[-1]),"close",4),findPriceFromDate(str(u[-1]),"close",5)]



futurePercentDiffs = {}
for k in range(len(futurePercDiff.keys())):
	futurePercentDiffs[list(futurePercDiff.keys())[k]] = percentDifSimple(futurePercDiff[list(futurePercDiff.keys())[k]])

weekDataImp = getData()
futurePrices = {}
for l in list(futurePercentDiffs.keys()):
	futurePrices[str(l)] = []
	for we in range(len(futurePercentDiffs[str(l)])):
		futurePrices[str(l)].append((float(futurePercentDiffs[l][we]) + 1)*weekDataImp["close"][-1])
	

print(f"Starting Price: {weekDataImp['close'][-1]}")
columnList = []
for lm in list(futurePrices.keys()):
	columnList.append(lm)
printingOrder = pd.DataFrame(futurePrices, columns = columnList)
print(printingOrder)
