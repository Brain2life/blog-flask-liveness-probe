from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

# Initial status and timestamp
status_info = {
    "status": "UP",
    "last_update_time": time.time()
}

def update_status():
    current_time = time.time()
    # Update status every 30 seconds
    if current_time - status_info["last_update_time"] >= 30:
        # Randomly choose a new status
        status_info["status"] = random.choice(["UP", "DOWN"])
        status_info["last_update_time"] = current_time

@app.route('/healthz', methods=['GET'])
def healthz():
    update_status()  # Check if it's time to update the status
    return jsonify({"status": status_info["status"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
