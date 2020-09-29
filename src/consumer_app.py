#!flask/bin/python
from flask import Flask, request, jsonify, abort
import requests

app = Flask(__name__)

@app.route('/consumer/api/items', methods=['GET'])
def get_items():
    response = requests.get("http://127.0.0.1:5000/provider/api/items")
    return response.text

@app.route('/consumer/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    url = "{}/{}".format("http://127.0.0.1:5000/provider/api/items", item_id)
    response = requests.get(url)
    return response.text

@app.route('/consumer/api/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        abort(400)
    response = requests.post('http://127.0.0.1:5000/provider/api/items', json = request.json)
    return response.text

if __name__ == '__main__':
    app.run(port = 5001, debug = True)