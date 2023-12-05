import flask
import socket
import os
import redis
import json

APP = flask.Flask(__name__)


@APP.route('/import', methods=['POST'])
def handle_import():
    try:
        data = json.loads(flask.request.data)
        version=os.environ.get('VERSION', 'Desconocida')
        print(json.dumps(data, indent=4))
    except Exception as e:
        print(f"Error processing message: {e}")
        return '', 500
    
    return flask.jsonify(data), 200


if __name__ == '__main__':
    PORT=os.environ['PORT']
    APP.debug = os.environ.get("DEBUG", True).upper() == "TRUE"
    APP.run(host='0.0.0.0', port=PORT)
