import requests

url = "http://localhost:5000/ping"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("API is working! Response:", response.json())
    else:
        print(f"Failed to reach the API. Status code: {response.status_code}")
except Exception as e:
    print("Error:", str(e))
