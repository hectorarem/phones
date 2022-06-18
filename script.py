import csv
import requests
import time
from devices_all import PHONES

res = []
res.append('model, name, usd price\n')
with open('phone_dataset .csv', newline='') as csvfile:
    phonesModels = csv.reader(csvfile)
    for r in phonesModels:
        print(r[1])
        url = f'http://127.0.0.1:8000/api/phone-detail/?model={r[1]}'
        response = requests.get(url)
        if response.ok:
            print(response.json())
            resp = response.json()[0]
            res.append(f'{resp["model"]}, {resp["name"]}, {round(resp["priceUSD"], 2)}\n')
        else:
            print(f"Error with {r[1]}")
            break
        time.sleep(60)

# for r in PHONES:
#     print(r['device'])
#     url = f'http://127.0.0.1:8000/api/phone-detail/?model={r["model"]}'
#     response = requests.get(url)
#     if response.ok:
#         print(response.json())
#         if len(response.json()) > 0:
#             resp = response.json()[0]
#             res.append(f'{resp["model"]}, {resp["name"]}, {round(resp["priceUSD"], 2)}\n')
#         else:
#             print(f"Modelo {r['model']} no encontrado en gsmarena")
#     else:
#         print(f"Error with {r['model']}")
#         break
#     time.sleep(60)

with open('devices-prices.csv', 'w') as file:
    file.writelines(res)
