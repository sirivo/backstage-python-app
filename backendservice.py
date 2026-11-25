from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/status", methods=["GET"])
def check_status():
  return jsonify({"server": "online", "tasks_pending": 0})


if __name__ == "__main__":
  app.run(port=5000)
