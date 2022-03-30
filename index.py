import json
from flask import Flask, Response, request
from black import format_str, FileMode

app = Flask(__name__)


def format_response(body, code=200):
    return


@app.route('/format', methods=['POST'])
def format():
    data = request.get_json()
    code = data.get('code', None)
    if (code):
        return Response(format_str(code, mode=FileMode()))
    return Response(json.dumps({'error': 'POST param code missing'}),
                    status=400)
