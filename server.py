import time
from time import sleep

from flask import Flask, jsonify, request
import mysql.connector
import threading


app = Flask(__name__)

# SQL Connection Helper
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="test",
        password="test",
        database="test"
    )

def create_ec2(instance_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    def update_status(status):
        cursor.execute("UPDATE ec2_instance SET status = %s WHERE instance_id = %s", (status, instance_id))
        conn.commit()
        print(f"[DB] {instance_id} -> {status}")

    update_status("INITIALIZING")
    time.sleep(15)

    update_status("ALLOCATING_RESOURCES")
    time.sleep(10)

    update_status("BOOTING_INSTANCE")
    time.sleep(15)

    update_status("RUNNING")

    cursor.close()
    conn.close()


@app.route('/create_ec2/<instance_id>')
def create_ec2_api(instance_id):
    print(">>> ENTER create_ec2_api", instance_id, flush=True)
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT IGNORE INTO ec2_instance (instance_id, status) VALUES (%s, %s)", (instance_id, "NOT_STARTED"))
    conn.commit()
    print(f"[DB] {instance_id} created with status NOT_STARTED")

    cursor.close()
    conn.close()

    #fire background thread
    thread = threading.Thread(target=create_ec2, args=(instance_id,))
    thread.start()

    return jsonify({
        "message": "EC2 instance started",
        "instance_id": instance_id
    })

@app.route('/get_status/<instance_id>')
def get_ec2_status(instance_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT status FROM ec2_instance WHERE instance_id = %s", (instance_id,))

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if not row:
        return jsonify({
            "message": "EC2 instance NOT FOUND",
        })

    return jsonify({
        "instance_id": instance_id,
        "status": row[0],
    })

@app.route('/wait_for_status/<instance_id>')
def wait_for_status(instance_id):
    last_known_status = request.args.get("last_status")
    timeout_seconds = 20
    poll_interval = 1

    start_time = time.time()

    while True:
        conn = get_db_connection()
        curser = conn.cursor()

        curser.execute("SELECT status FROM ec2_instance WHERE instance_id = %s", (instance_id,))
        row = curser.fetchone()
        if not row:
            return jsonify({"status": "NOT_FOUND",
                            "instance_id": instance_id,})

        current_status = row[0]

        if current_status != last_known_status:
            return jsonify({"instance_id": instance_id,
                            "status": current_status,
                            "changed": True})

        if time.time() - start_time > timeout_seconds:
            return jsonify({"instance_id": instance_id,
                            "status": current_status,
                            "changed": False,
                            "Timeout": True})
        sleep(poll_interval)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)


