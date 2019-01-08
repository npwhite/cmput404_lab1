import requests

print(requests.__version__)

r = requests.get(google)
print(r.satus_code)
print(r.headers)

girhub_url = ".../main.py" # fill in ...'s based on your github path to main.py after pushing
r = requests.get(github_url)
print(r.text)

