#importinng modules
import requests
import sys

#checking the command line argument
if sys.argv != 2:
    sys.exit("missing the command line argument")
#get the number of bitcoins from command line argument
else:
    try:
        number = float(sys.argv[1])
    except:
        sys.exit("invalied command line argument")

#get bitcoin price from the request module
try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    sys.exit()

#get the price of a bitcoin
res = response.json()
price = float(res['bpi']['USD']['rate'].replace(',',''))

#get the total value 
total = number*price

print(f"${total:,.4f}")