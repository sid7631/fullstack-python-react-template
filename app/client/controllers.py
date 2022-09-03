from flask import current_app as app, Blueprint, send_from_directory
from flask_login import login_required

frontend = Blueprint('frontend', __name__, url_prefix='/frontend/')

@frontend.route('/', defaults={'path':''})
@frontend.route('/<path:path>')
@login_required
def frontend_view(path):
    print(app.static_folder)
    return send_from_directory(app.static_folder, 'index.html')