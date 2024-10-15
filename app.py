"""
A sample Hello World server.
"""
import os

from flask import Flask, render_template, jsonify
from inventory import inventory

# pylint: disable=C0103
app = Flask(__name__)

@app.route('/inventory', methods=['GET'])
def inventory_list():
    """Return a list of inventory items in JSON format."""
    return jsonify(inventory)

@app.route('/inventory/<productid>', methods=['GET'])
def inventory_item(productid):
    """Return a single inventory item in JSON format."""
    for item in inventory:
        if item['productid'] == productid:
            return jsonify(item)
    return jsonify({'error': 'Product not found'}), 404

    
@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = "It's running!"

    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')

    return render_template('index.html',
        message=message,
        Service=service,
        Revision=revision)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
