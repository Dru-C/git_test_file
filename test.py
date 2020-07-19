
import sys
import requests
import pandas as pd

print(sys.version)
print(sys.executable)


def greet(who_to_great):
    greeting = f'Hello, {who_to_great}'
    return greeting


r = requests.get('https://dru-c.github.io/My_Portfolio/')
#r = requests.get('https://coreyms.com')
print(r.status_code)

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

print(df)
