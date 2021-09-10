import os
os_env = os.environ
binance_api = os_env['binance_api']
binance_secret = os_env['binance_secret']

from binance.spot import Spot 

client = Spot()
print(client.time())

client = Spot(key=f'{binance_api}', secret=f'{binance_secret}')

# Get account information
client_account = client.account()
account_balances = client_account['balances']
account_asset = [ item['asset'] for item in account_balances]
print(len(account_asset))

