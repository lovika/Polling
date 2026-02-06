import time
import requests

INSTANCE_ID = "1"

requests.get(f"http://127.0.0.1:5000/create_ec2/{INSTANCE_ID}")

while True:
    r = requests.get(f"http://127.0.0.1:5000/get_status/{INSTANCE_ID}")
    status = r.json()["status"]
    print("STATUS: ", status)

    if status == "RUNNING":
        print("Instance is running. Stop Polling.")
        break

    print("Polling again in 2 seconds...")
    time.sleep(2)