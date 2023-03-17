import requests

endpoint = 'http://localhost/blog-yii-2-bootstrap-3/apirest/articulos'

# header = {'content-type': 'application/json', 'token': '3qrrrw3242'}
# response = requests.get(endpoint, headers = header)

response = requests.get(endpoint, timeout = 30)

# print(response.text)
# print(response.json())

for value in response.json():
    #print(value, end='\n')
    print(f"[{value['id']}] {value['titulo']}")