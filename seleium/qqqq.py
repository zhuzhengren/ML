import requests

url = "https://postman-echo.com/time/unit"

querystring = {"timestamp":"2016-10-10","unit":"day"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "ecd642a2-bdd6-e6fa-1028-dcc2538af001"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)