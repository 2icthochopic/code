#Takes inputs of Entry, Stop-Loss, and Take-Profit price(s);
#Calculates Average Take-Profit price, Reward/Risk Ratio, # of contracts to trade at which leverage, and Maximum Drawdown.
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("-------------------------")
avgEntry = float(input('Average Entry Price? '))
stopLoss = float(input('Stop Loss Price? '))
print("-------------------------")
tps = int(input('# of Take Profits? '))
print("-------------------------")
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
print("-------------------------")
rr = abs(avgEntry - avgTP) / abs(avgEntry - stopLoss)
# Then it figures out max drawdown (aka % to stop loss)
mdd = abs(avgEntry - stopLoss)*100 / avgEntry
# USD worth of entire account?
equity = float(input('Total equity? '))
# How much of equity to risk on this one trade?
risk = float(input('Risk %? '))*0.01
leverage = round((risk * equity) / (mdd * 0.01) / equity, 2)
if leverage > 100:
	leverage = 100
contracts = round((risk * equity) / (mdd * 0.01))
if contracts > leverage * equity:
	contracts = leverage * equity

# long or short?
if avgEntry > avgTP:
	longed = False
	trade_direction = 'SHORT POSITION'
else: 
	longed = True
	trade_direction = 'LONG POSITION'

options = Options()
options.headless = True
browser = webdriver.Chrome('/Users/JonathanMac/Dev/code/chromedriver',options=options)
browser.implicitly_wait(30)
browser.get('https://www.bitmex.com/app/trade/XBTUSD')

side_bar = browser.find_element_by_css_selector('.orderOptionsDropdown .dropdown-toggle-icon')
side_bar.click()

open_calc = browser.find_element_by_css_selector('.openCalculator')
open_calc.click()

liquidation_calculator = browser.find_element_by_css_selector('.title > .nav > li:nth-child(3) .innerTitle')
liquidation_calculator.click()

isolated_margin = browser.find_element_by_css_selector('.is-checked > .button')
isolated_margin.click()

quantity_field = browser.find_element_by_id('quantity')
quantity_field.send_keys(str(contracts))

entry_price_field = browser.find_element_by_id('entryPrice')
entry_price_field.send_keys(str(avgEntry))

leverage_field = browser.find_element_by_id('leverage')
leverage_field.send_keys(str(leverage))

liquidation_price_1 = browser.find_element_by_css_selector('.gridRow:nth-child(3) > .gridCell:nth-child(2)')

# If longed = True: liquidation_price_1.text should be less than entry_price_field.text
# If longed = False: liquidation_price_1.text should be greater than entry_price_field.text

long_toggle = browser.find_element_by_css_selector('.labeledSwitch:nth-child(1) > .leftLabel')
short_toggle = browser.find_element_by_css_selector('.labeledSwitch:nth-child(1) > .rightLabel')

if longed == True and float(liquidation_price_1.text) > avgEntry:
	long_toggle.click()
	position_liquidation_price = liquidation_price_1.text

elif longed == True and float(liquidation_price_1.text) < avgEntry:
	position_liquidation_price = liquidation_price_1.text

elif longed == False and float(liquidation_price_1.text) > avgEntry:
	position_liquidation_price = liquidation_price_1.text

else:
	short_toggle.click()
	position_liquidation_price = liquidation_price_1.text

browser.quit()

print("-------------------------")
print(f'{trade_direction}')
print("Contracts: {}".format(contracts))
print("Leverage: {}x".format(leverage))
print(f"Entry: {avgEntry}")
print(f"Stop Loss: {stopLoss}")
if longed == True:
	if float(position_liquidation_price) > stopLoss:
		safety = ("(UNSAFE)")
	else: 
		safety = ("(Safe)")
if longed == False:
	if float(position_liquidation_price) < stopLoss:
		safety = ("(UNSAFE)")
	else:
		safety = ("(Safe)")
print(f"Liquidation Price: {position_liquidation_price}  {safety}")
print("Max Drawdown: {}%".format(round(mdd, 2)))
print("R:R: {}".format(round(rr, 2)))
print("-------------------------")
clear_command = input("clear?")