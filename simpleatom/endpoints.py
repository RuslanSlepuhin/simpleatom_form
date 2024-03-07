import asyncio
import os
from flask import Flask, send_from_directory
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

        # @app.route("/.well-known/acme-challenge/<path:filename>", methods=['GET'])
        # async def sdsa(filename):
        #     path = "/root/simpleatom_form/static"
        #     return send_from_directory(path, filename)

        @app.route('/<path:path>')
        def serve_challenge(path):
            if path.startswith('.well-known/acme-challenge/'):
                filename = path.split('/')[-1]
                if filename == '9mOnzU7vV1RSQkcfsnY2RTkDuBtvYACbmJbsxW5I3nk':
                    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), '9mOnzU7vV1RSQkcfsnY2RTkDuBtvYACbmJbsxW5I3nk.txt')
                if filename == '3zBWhkXcCIEzwBXkMtMtsChZONKlfrmB7Z29bMSXqPk':
                    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), '3zBWhkXcCIEzwBXkMtMtsChZONKlfrmB7Z29bMSXqPk.txt')

            return "Not found", 404

    app.run(host="127.0.0.1", port=int(os.environ.get('PORT', 8000)))


def run_endpoints():
    endpoints = Endpoints()
    asyncio.run(endpoints.main_endpoints())
