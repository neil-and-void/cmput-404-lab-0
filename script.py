import requests

print(requests.__version__) # 2.28.1

res = requests.get('')

print(res.text)
