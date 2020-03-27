from werkzeug.exceptions import abort
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('Main', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        choice = request.form['choice']
        if int(choice) == 1:
            return redirect(url_for('Main.Bennington_Scene1'))
        elif int(choice) == 2 :
            return redirect(url_for('Main.hallway'))
    return render_template('index.html')

@bp.route('/Bennington_Scene1', methods=('GET', 'POST'))
def Bennington_Scene1():
    if request.method == 'POST':
        if int(choice) == 1:
            return redirect(url_for('Main.Bennington_Scene1Act1'))
        elif int(choice) == 2:
            return redirect(url_for('Main.Bedroom'))
        elif int(choice) == 3:
            return redirect(url_for('Main.index'))
        elif int(choice) == 2:
    return render_template('Mr.Bennington_Scene1/Bennington_Scene1.html')
