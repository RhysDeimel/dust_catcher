import json
from httpserver import HTTPServer, HTTPResponse
import fan

app = HTTPServer()


@app.route("GET", "/")
def root(conn, request):
    response = HTTPResponse(200, "application/json", close=True)
    response.send(conn)

    data = {
        "temperature": None,
        "humidity": None,
        "fan_speed": fan.PWMFan().speed,  # the duty cycle (between 0 and 100)
    }

    conn.write(json.dumps(data))


@app.route("PUT", "/")
def update(conn, request):
    data = request.body.decode("utf-8")
    data = json.loads(data)

    fan.PWMFan().speed = data["fan_speed"]

    response = HTTPResponse(204, close=True)
    response.send(conn)
