from flask import Blueprint, jsonify

common = Blueprint('common', __name__)


@common.route('/', methods=['GET'])
def index():
    return jsonify({"service": "Desafio Backend",
                    "made for":"Rafael Ramos",
                    "version": "1.0"})
