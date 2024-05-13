import requests

url_sql = "https://api.opendota.com/api/explorer"
url_schema = "https://api.opendota.com/api/schema"


# params = {
#   "sql": "SELECT * FROM matches WHERE LIMIT 2"
# }

# response = requests.get(url=url_sql, params=params)

# print(response.text)

response = requests.get(url=url_schema)

print(response.text)