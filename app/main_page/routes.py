import json
from wsgiref import headers
from flask import current_app, request,render_template
from flask.json import jsonify
from app.main_page import main_page


# @main_page.route('/', methods=["GET"])
# def index():
#     headers=[]
#     print(request.headers)
#     for i in request.headers:
#         headers.append(i)
#     print(headers)
#     return jsonify(headers)

@main_page.route('/',methods=["GET"])
def show_index():
#     headers=[]
#     print(request.headers)
#     for i in request.headers:
#         headers.append(i)
    return render_template('index.html')