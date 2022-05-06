from flask import Flask, request
from flask_restful import Api
import json
import requests
import logging

logger = logging.getLogger(__name__)


app = Flask(__name__)
api = Api(app)
@app.route('/weather')
def weather():
    city_name = request.args.get('city')
    api_key = "157fed6fdfe4cf25058b936e5e04a5b3"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    logger.info(response.json())
    return response.json()


if __name__ == '__main__':
     app.run(host="0.0.0.0",port='3002',threaded=True,debug=True)