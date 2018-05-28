import os
from flask import Flask

from app import create_app


config_name = os.environ.get('FLASK_CONFIG')
app = create_app(config_name)
host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', 8080))

if __name__ == "__main__":
    app.run(host=host, port=port)