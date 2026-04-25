from flask import Flask, jsonify
import os
import socket
import redis

app = Flask(__name__)

cache = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379)

@app.route("/")
def index():
    try:
        visits = cache.incr("visits")
    except Exception:
        visits = "unavailable"
    return f"<h1>GitHub Cloud Lab</h1><p>Visits: {visits}</p>"

@app.route("/info")
def info():
    return jsonify({
        "hostname": socket.gethostname(),
        "environment": os.environ.get("APP_ENV", "development")
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
