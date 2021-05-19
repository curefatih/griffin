from os.path import join

from flask import Blueprint, render_template, current_app

from app import db, client
from app.utils import get_user_info

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
def index():
    return 'Ok\n'


@api.route('/send_weekly')
def send_weekly():
    query = open(join(current_app.config['BASEDIR'], 'app', 'templates', 'assets', 'query.sql'), 'r').read()
    result = db.engine.execute(query)
    result = get_user_info(result)
    message = render_template('assets/message_detail.txt', result=result)
    client.chat_postMessage(link_names=1, channel='#general', text=message)

    return 'Ok\n'
