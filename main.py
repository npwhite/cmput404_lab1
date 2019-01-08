import requests

print(requests.__version__)

r = requests.get("http://google.com/")
print(r.status_code)
#print(r.headers)

github_url = "https://raw.githubusercontent.com/npwhite/cmput404_lab1/master/main.py"
r = requests.get(github_url)
print(r.text)

