from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data for demonstration
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({"items": items})

# Get a specific item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item not found"}), 404

# Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = {"id": len(items) + 1, "name": request.json.get('name')}
    items.append(new_item)
    return jsonify(new_item), 201

# Update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        item['name'] = request.json.get('name')
        return jsonify(item)
    return jsonify({"message": "Item not found"}), 404

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)
