import csv
import requests
import time

res = []
res.append('model, name, usd price\n')
with open('devices.csv', newline='') as csvfile:
    phonesModels = csv.reader(csvfile)
    for r in phonesModels:
        print(r[1])
        url = f'http://127.0.0.1:8003/api/phone-detail/?model={r[1]}'
        response = requests.get(url)
        if response.ok:
            print(response.json())
            resp = response.json()[0]
            res.append(f'{resp["model"]}, {resp["name"]}, {round(resp["priceUSD"], 2)}\n')
        else:
            print(f"Error with {r[1]}")
            break
        time.sleep(60)

with open('devices-prices.csv', 'w') as file:
    file.writelines(res)
