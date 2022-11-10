from flask import Flask
from flask import render_template
from flask import abort
import requests as req
import json
app = Flask(__name__)
 
@app.route('/convert/')
@app.route('/convert/<base>/<to>/<amount>')
 
def convert(base=None, to=None, amount=None):
    currency = base + to
    r = req.get('https://api.finage.co.uk/last?currencies='+currency+'&apikey=API_KEYf3emOSjHpsbh5lr7FNW17gA1cRw4j3SBw1cC6QrxFVjqEK')
    response = json.loads(r.text)
    calculation = "%.2f" % (response["currencies"][0]["value"] * float(amount))
    value = response["currencies"][0]["value"]
    change = "%.2f" % (response["currencies"][0]["change"])
    difference = "%.2f" % (response["currencies"][0]["difference"])
    last_update = response["lastUpdate"]
 
    return render_template('index.html', base=base.upper(), to=to.upper(), value = value, calculation = calculation, amount=amount, change=change, difference = difference, last_update=last_update)
