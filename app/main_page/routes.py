import json
import os

from wsgiref import headers

from app.main_page import main_page
from flask import current_app, redirect, render_template, request, url_for
from flask.json import jsonify
from ua_parser import user_agent_parser
from werkzeug.utils import secure_filename

# @main_page.route('/', methods=["GET"])
# def index():
#     headers=[]
#     print(request.headers)
#     for i in request.headers:
#         headers.append(i)
#     print(headers)
#     return jsonify(headers)


@main_page.route('/fireware', methods=["GET"])
def fireware():
    return render_template('fireware.html')


@main_page.route('/', methods=["GET"])
def show_index():
    res = []
    ios = [{'field': 'CVE-2022-31009',
           'data': 'wire-ios is an iOS client for the Wire secure messaging application.Invalid accent colors of Wire communication partners may render the iOS Wire Client partially unusable by causing it to crash multiple times on launch. These invalid accent colors can be used by and sent between Wire users.'}]
    ios_cvss = [{
        'id': 'CVE-2022-31009',
        'pub_date': '2022-06-23',
        'score': '4.0'
    }]
    samsung = [
        {
            'field': 'CVE-2016-4032',
            'data': 'Samsung SM-G920F build G920FXXU2COH2 (Galaxy S6), SM-N9005 build N9005XXUGBOK6 (Galaxy Note 3), GT-I9192 build I9192XXUBNB1 (Galaxy S4 mini), GT-I9195 build I9195XXUCOL1 (Galaxy S4 mini LTE), and GT-I9505 build I9505XXUHOJ2 (Galaxy S4) devices do not block AT+USBDEBUG and AT+WIFIVALUE, which allows attackers to modify Android settings by leveraging AT access, aka SVE-2016-5301.'
        }
    ]
    samsung_cvss = [{
        'id': 'CVE-2016-4032',
        'pub_date': '2017-04-13',
        'score': '2.1'
    }]
    cve = []
    cvss = []
    for i in request.headers:
<<<<<<< HEAD
        # print(i)
        # headers.append({'field': i[0], 'data': i[1]})
        # headers.append(i)
        if i[0] == "User-Agent":
            UA = user_agent_parser.Parse(i[1])
            print(UA)
            res.append(
                {'field': "Browser", 'data': UA['user_agent']['family']+UA['user_agent']['major']})
            res.append(
                {'field': "OS", 'data': UA['os']['family']+UA['os']['major']})
            res.append({'field': 'Device', 'data': UA['device']['family']})

            if UA['device']['family'] in 'iPhone':
                cve = ios
                cvss = ios_cvss
            elif UA['device']['brand'] in 'Samsung':
                cve = samsung
                cvss = samsung_cvss
            else:
                cve = [{
                    'field': 'Data waiting for update',
                    'data': 'Data waiting for update'
                }]
                cvss = [{
                    'id': 'Data waiting for update',
                    'pub_date': 'Data waiting for update',
                    'score': 'Data waiting for update'
                }]

    return render_template('index.html', ua=res, cve=cve, cvss=cvss)
=======
        headers.append(i)
        if i[0]=="User-Agent":
            UA=user_agent_parser.Parse(i[1])
            print(UA)
    # print(headers)
    
    return render_template('index.html',User_Agent=UA["user_agent"])
>>>>>>> parent of dd72ef1 (Add more complex template)
