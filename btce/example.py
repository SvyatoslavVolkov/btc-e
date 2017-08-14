#!/usr/bin/env python
# BTC-e API Class (Example Script)
# Developed by acidvegas in Python
# https://github.com/acidvegas/btce
# example.py

'''
Here is an example script that uses both the Public API & Trade API.
The script will retrieve your balance for each coin and the total sum.
Coins with no balance are not showed.
'''

from btce import public_api, trade_api

# API Keys
api_key    = 'CHANGEME'
api_secret = 'CHANGEME'
nonce      = 1

# Main
tapi = trade_api(api_key, api_secret, nonce)
info = tapi.getInfo()
if info['success']:
	funds = info['return']['funds']
	total = 0.00
	print('COIN   BALANCE     PRICE        VALUE')
	for coin in funds:
		if funds[coin]:
			balance = '{0:.2f}'.format(funds[coin])
			price   = '{0:.2f}'.format(public_api.ticker(coin, 'usd')[f'{coin}_usd']['sell'])
			value   = '{0:.2f}'.format(float(balance) * float(price))
			total += float(value)
			print('{0}{1}${2}${3}'.format(coin.ljust(7, ' '), balance.ljust(12, ' '), price.ljust(12, ' '), value))
	print('Total: ${0:.2f}'.format(total))
else:
	print('[!] Error - ' + info['error'])