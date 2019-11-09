# Updated version of pSize
# Added ability to input any number of Take Profits
# Calculates average TP and Reward/Risk
print("---------------------")
avgEntry = float(input('Average Entry? '))
stopLoss = float(input('Stop Loss? '))
print("---------------------")
tps = int(input('# of Take Profits? '))
print("---------------------")
tpNumber = range(0,tps)
tpList = list()
tpPercents = list()
for n in range(len(tpNumber)):
	nAdjusted = int(n) + 1
	tp = input(f'TP {nAdjusted}: ')
	portion = input(f'%: ')
	print(" ")
	tpList.append(tp)
	tpPercents.append(portion)	
tpCalc = list()
for x in range(len(tpList)):
	xAdjusted = int(x)
	tpCalc.append(float(tpList[xAdjusted]) * (float(tpPercents[xAdjusted]) / 100))
avgTP = round(sum(tpCalc), 2)
print(f'Average TP: {avgTP}')
print("---------------------")
rr = abs(avgEntry - avgTP) / abs(avgEntry - stopLoss)
# Then it figures out max drawdown (aka % to stop loss)
mdd = abs(avgEntry - stopLoss)*100 / avgEntry
# USD worth of entire account?
equity = float(input('Total equity? (Total Account Value in USD) '))
# How much of equity to risk on this one trade?
risk = float(input('Risk %? (How much of equity to risk on this one trade) '))*0.01
leverage = round((risk * equity) / (mdd * 0.01) / equity, 2)
contracts = round((risk * equity) / (mdd * 0.01))
print("---------------------")
print("Contracts: {}".format(contracts))
print("Leverage: {}x".format(leverage))
print("Max Drawdown: {}%".format(round(mdd, 2)))
print("R:R: {}".format(round(rr, 2)))
print("---------------------")
