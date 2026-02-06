import time
from flask import Flask, jsonify
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

if __name__ == '__main__':
    app.run(debug=True, threaded=True)


