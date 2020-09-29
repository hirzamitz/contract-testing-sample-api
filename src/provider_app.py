#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

items = [
    {
        'id': 1,
        'name': u'Strawberries',
        'type': u'Grocery', 
        'price': 5.00,
        'count': 2
    },
    {
        'id': 2,
        'name': u'Carrots',
        'type': u'Grocery', 
        'price': 4.00,
        'count': 3.50
    }
]

@app.route('/provider/api/items', methods=['GET'])
def get_items():
    return jsonify({'items': items})

@app.route('/provider/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = [item for item in items if item['id'] == item_id]
    if len(item) == 0:
        abort(404)
    return jsonify({'item': item[0]})

@app.route('/provider/api/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        abort(400)
    item = {
        'id': items[-1]['id'] + 1,
        'name': request.json['name'],
        'type': request.json.get('type', ""),
        'price': request.json.get('price', ""),
        'count': request.json.get('count', "")
    }
    items.append(item)
    return jsonify({'item': item}), 201

@app.route('/provider/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = [item for item in items if item['id'] == item_id]
    if len(item) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    if 'type' in request.json and type(request.json['type']) is not str:
        abort(400)
    if 'price' in request.json and type(request.json['price']) is not float:
        abort(400)
    if 'count' in request.json and type(request.json['count']) is not int:
        abort(400)
    item[0]['name'] = request.json.get('name', item[0]['name'])
    item[0]['type'] = request.json.get('type', item[0]['type'])
    item[0]['price'] = request.json.get('price', item[0]['price'])
    item[0]['count'] = request.json.get('count', item[0]['count'])
    return jsonify({'item': item[0]})

@app.route('/provider/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = [item for item in items if item['id'] == item_id]
    if len(item) == 0:
        abort(404)
    items.remove(item[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
    
if __name__ == '__main__':
    app.run(debug = True)