from werkzeug.exceptions import abort
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('Main', __name__)

@bp.route('/')
def index():
    return render_template('Game/index.html')
