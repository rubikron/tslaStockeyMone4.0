from yahoo_finance_api2 import share
from datetime import datetime
import pandas as pd

def getData(dayLen = 7):
	stock = share.Share("TSLA")
	weekData = dict(stock.get_historical(share.PERIOD_TYPE_DAY,dayLen,share.FREQUENCY_TYPE_DAY,1))
	for x in range(len(weekData["timestamp"])):
		timestamp = int(str(int(int((weekData["timestamp"][x]))/1000)))
		dt_object = datetime.fromtimestamp(timestamp)
		dt_object = str(dt_object)
		dt_object = dt_object[:10]
		someDict = weekData
		weekData["timestamp"][x] = dt_object
		
	return dict(weekData)

def percentDif(datasetWithDateAndCategory,category):
	lenOfDataset = len(datasetWithDateAndCategory[category])
	percentDiffsList = []
	for x in range(lenOfDataset - 1):
		percentDiffsList.append([(datasetWithDateAndCategory[category][x+1] - datasetWithDateAndCategory[category][x])/datasetWithDateAndCategory[category][x],datasetWithDateAndCategory['timestamp'][x],datasetWithDateAndCategory['timestamp'][x+1]])
	return percentDiffsList

