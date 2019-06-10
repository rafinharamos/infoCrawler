# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify
from crawler import auth, crawler

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/', methods=['GET'])
@auth.login_required
def index():
    file_name = 'feed.xml'
    crawler.create_update_file_xml(file_name)
    process_itens_xml = crawler.process_file_xml(file_name)
    feed = crawler.process_html_content(process_itens_xml)
    return jsonify(feed=feed)
