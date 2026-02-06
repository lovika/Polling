import requests


INSTANCE_ID = "1"

requests.get(f"http://127.0.0.1:5000/create_ec2/{INSTANCE_ID}")

while True:
    r = requests.get(f"http://127.0.0.1:5000/get_status/{INSTANCE_ID}")

    last_known_status = r.json()["status"]
    print(f"last_known_status: {last_known_status}")

    new_status = requests.get(f"http://127.0.0.1:5000/wait_for_status/{INSTANCE_ID}",
                              params={"last_status": last_known_status})

    data = new_status.json()
    print(f"new_status response: {data}")

    if (data["status"] == "RUNNING"):
        print("EC2 is ready. Stopping long polling.")
        break



