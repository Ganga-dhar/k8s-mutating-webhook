from flask import Flask, request, jsonify
import base64
import json

app = Flask(__name__)

@app.route('/mutate', methods=['POST'])
def mutate():
    admission_review = request.get_json()
    uid = admission_review['request']['uid']

    patch = [{
        "op": "add",
        "path": "/metadata/labels/app-owner",
        "value": "platform-team"
    }]

    response = {
        "response": {
            "uid": uid,
            "allowed": True,
            "patchType": "JSONPatch",
            "patch": base64.b64encode(json.dumps(patch).encode()).decode()
        }
    }
    return jsonify(response)

app.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'))
