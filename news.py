from flask import Flask, request
from flask_restful import Api
import json
import requests
import logging

app = Flask(__name__)
api = Api(app)
logger = logging.getLogger(__name__)


@app.route('/news')
def news():
    country_name = request.args.get('country')
    api_key = "9973b41453fd4f7fbdf46e663c30f0aa"
    base_url = "http://newsapi.org/v2/top-headlines?"
    complete_url = base_url + "country=" + country_name + "&apiKey=" + api_key
    response = requests.get(complete_url)
    logger.info(response.json())
    return response.json()


if __name__ == '__main__':
     app.run(host="0.0.0.0",port='3003',threaded=True,debug=True)