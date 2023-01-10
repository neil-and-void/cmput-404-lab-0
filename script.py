import requests

print(requests.__version__) # 2.28.1

res = requests.get('https://raw.githubusercontent.com/neilZon/cmput-404-lab-0/main/script.py')

print(res.text)
