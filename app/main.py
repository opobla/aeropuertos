import flask
import socket
import os
import redis
import json
import logging
from google.cloud import logging as gcp_logging

# Configura el cliente de Cloud Logging
client = gcp_logging.Client()
logger = client.logger('aeropuertos-log')

# Configura el logger de Python para redirigir los logs a Cloud Logging
# cloud_handler = gcp_logging.handlers.CloudLoggingHandler(client, name='aeropuertos-log')
#cloud_handler.setLevel(logging.INFO)

# Añade el CloudLoggingHandler al logger
#logger.addHandler(cloud_handler)



APP = flask.Flask(__name__)


@APP.route('/import', methods=['POST'])
def handle_import():
    try:
        data = json.loads(flask.request.data)
        version=os.environ.get('VERSION', 'Desconocida')
        logger.info("*** Recibida petición de importación ***")
        logger.log_struct(data, severity='INFO')

    except Exception as e:
        print(f"Error processing message: {e}")
        return '', 500
    
    return flask.jsonify(data), 200


if __name__ == '__main__':
    PORT=os.environ['PORT']
    APP.debug = os.environ.get("DEBUG", "True").upper() == "TRUE"
    APP.run(host='0.0.0.0', port=PORT)
