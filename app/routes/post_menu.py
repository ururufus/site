from flask import Blueprint, render_template, request, redirect
from ..extensions import db
from ..models.post_menu import PostMenu

post_menu = Blueprint('post_menu', __name__)

@post_menu.route('/menu', methods = ['POST', 'GET'])
def create():
    if request.method == 'POST':
        menu = request.form['menu']
        post_menu = PostMenu(name = menu)
        try:
            db.session.add(post_menu)
            db.session.commit()
        except Exception as e:
            print(str(e))
        return redirect('/menu')
    else:
        return render_template('menu/menu.html')