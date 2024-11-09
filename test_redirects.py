import requests

url="https://www.woolworths.com.au/christmas-bonbons"

x = requests.get(url, headers={"User-Agent":"py"})

print(x.status_code)
print(x.is_permanent_redirect)
print(x.url)
