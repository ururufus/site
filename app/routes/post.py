from flask import Blueprint, render_template, request, redirect
from ..extensions import db
from ..models.post import Post

post = Blueprint('post', __name__)

@post.route('/post/create', methods = ['POST', 'GET'])
def create():
    if request.method == 'POST':
        song = request.form['song']
        post = Post(name = song)
        try:
            db.session.add(post)
            db.session.commit()
        except Exception as e:
            print(str(e))
        return redirect('/post/create')
    else:
        return render_template('songs/songs.html')