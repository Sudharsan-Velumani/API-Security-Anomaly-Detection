import requests
import time

url = "http://localhost:5000/predict"
data = {"data": [1, 2, 3, 4, 5]}  # Replace with test data

def measure_response_time():
    response_times = []

    for _ in range(100):
        start_time = time.time()
        response = requests.post(url, json=data)
        end_time = time.time()

        if response.status_code == 200:
            response_times.append(end_time - start_time)
        else:
            print(f"Request failed with status code: {response.status_code}")

    if response_times:
        print("Median Response Time:", sorted(response_times)[len(response_times) // 2])
        print("99th Percentile Response Time:", sorted(response_times)[int(len(response_times) * 0.99) - 1])
        print("Max Response Time:", max(response_times))
    else:
        print("No successful responses recorded.")

if __name__ == "__main__":
    measure_response_time()
