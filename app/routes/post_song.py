from flask import Blueprint, render_template, request, redirect
from ..extensions import db
from ..models.post_song import PostSong

post_song = Blueprint('post_song', __name__)

@post_song.route('/song', methods = ['POST', 'GET'])
def create():
    if request.method == 'POST':
        song = request.form['song']
        post = PostSong(name = song)
        try:
            db.session.add(post)
            db.session.commit()
        except Exception as e:
            print(str(e))
        return redirect('/song')
    else:
        return render_template('songs/songs.html')