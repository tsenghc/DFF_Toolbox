import json
from wsgiref import headers
from flask import current_app, request,render_template
from flask.json import jsonify
from app.main_page import main_page
from ua_parser import user_agent_parser

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
    headers=[]

    for i in request.headers:
        headers.append(i)
        if i[0]=="User-Agent":
            UA=user_agent_parser.Parse(i[1])
            print(UA)
    # print(headers)
    
    return render_template('index.html',User_Agent=UA["user_agent"])