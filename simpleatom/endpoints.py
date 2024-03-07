import asyncio
import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


class Endpoints:
    def __init__(self):
        self.db_request = None

    async def main_endpoints(self):

        @app.route("/", methods=['GET'])
        async def get_by_id():
            return {'error': 'hello'}

    app.run(host="127.0.0.1", port=int(os.environ.get('PORT', 8000)))


def run_endpoints():
    endpoints = Endpoints()
    asyncio.run(endpoints.main_endpoints())
