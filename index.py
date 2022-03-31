import json
import re
from flask import Flask, Response, request
import black

app = Flask(__name__)


def format_response(body, code=200):
    return


@app.route('/format', methods=['POST'])
def format():
    data = request.get_data()
  
    # Decode the bytes string
    code = data.decode("utf-8")
    if (code):
        formatted = black.format_str(
          code,
          mode=black.Mode(
            target_versions={black.TargetVersion.PY39}
          )
        )
        print(formatted)
        return Response(formatted)
    return Response(json.dumps({'error': 'POST param code missing'}),
                    status=400)
