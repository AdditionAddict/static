from flask import (
    Blueprint, render_template
)

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('main/index.html',
                           title='Flask-PWA')


@bp.route('/timesheet')
def timesheet():
    return render_template('main/timesheet.html',
                           title='Flask-PWA')