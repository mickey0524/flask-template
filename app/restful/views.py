from flask import jsonify
from flask import request as req
from app.restful import restful

@restful.route('/')
def index():
  obj = { 'baihao': 'ok' }
  return jsonify(
    message = "ok",
    data = obj
  )

@restful.route('/<name>/', methods = ['GET', 'POST'])
def param_index(name):
  age = req.values.get('age')
  return jsonify(
    message = 'ok',
    name = name,
    age = age
  )

@restful.route('/raw_json', methods = ['POST'])
def raw_json():
  name = req.json['name']
  return jsonify(
    message = 'ok'
  )

