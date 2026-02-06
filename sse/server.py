import threading
import time
from deployment import start_deployment

from flask import Flask, jsonify, Response, send_from_directory

app = Flask(__name__)

LOG_FILE = "sse/logs/deploy-1.log"


@app.route("/run_deployment")
def run_deployment():
    thread = threading.Thread(target=start_deployment, args=(LOG_FILE,))
    thread.start()
    return jsonify({"message":"Deployment started"})

@app.route("/stream_logs")
def stream_logs():
    def generate():
        with open(LOG_FILE, "r") as f:
            f.seek(0)

            while True:
                line = f.readline()
                if line:
                    # SSE format
                    yield f"data: {line.strip()}\n\n"
                else:
                    time.sleep(1)

    return Response(generate(), mimetype="text/event-stream")

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001, threaded=True)