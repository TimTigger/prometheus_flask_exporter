import random
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
PrometheusMetrics(app)

# 定义成功率阈值
success_rates = {
    "one": 0.20,  # 20%的成功率
    "two": 0.40,  # 40%的成功率
    "three": 0.60,  # 60%的成功率
    "four": 0.80,  # 80%的成功率
}

@app.route("/one")
def first_route():
    if random.random() < success_rates["one"]:
        return "ok"
    else:
        return ":(", 500

@app.route("/two")
def the_second():
    if random.random() < success_rates["two"]:
        return "ok"
    else:
        return ":(", 500

@app.route("/three")
def test_3rd():
    if random.random() < success_rates["three"]:
        return "ok"
    else:
        return ":(", 500

@app.route("/four")
def fourth_one():
    if random.random() < success_rates["four"]:
        return "ok"
    else:
        return ":(", 500

@app.route("/error")
def oops():
    return ":(", 500

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, threaded=True)