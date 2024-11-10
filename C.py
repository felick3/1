import requests
from flask import flask
p = 1
for i in range(10):
    print(p)
    p+=1
t = requests.get('https://github.com/felick3/1.git').text
print(t)