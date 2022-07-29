import json
from wsgiref import headers
from flask import current_app, request
from flask.json import jsonify
from app.main_page import main_page


@main_page.route('/', methods=["GET"])
def index():
    headers=[]
    print(request.headers)
    for i in request.headers:
        headers.append(i)
    print(headers)
    return jsonify(headers)
