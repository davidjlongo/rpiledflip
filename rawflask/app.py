#!flask/bin/python
from flask import Flask, abort, request
import json
import ledcontrol
import os

app = Flask(__name__)

led = "green"

@app.route('/', methods=['GET','POST','PUT'])
def index():
    if request.method == 'GET':
        return ledcontrol.read(led)

    elif request.method == 'POST':
        return ledcontrol.control(led,1)

    elif request.method == "PUT":
        if not request.json:
           abort(400)
        data = request.data
        dataDict = json.loads(data)
        shift = int(os.environ["HOSTNAME"][9:])
        value = (int(dataDict["value"]) >> shift) & 1
        ledcontrol.control(led,"on" if value else "off")
        return "Set LED to: "+ str(value) + "\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=False)
