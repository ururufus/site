from flask import Blueprint, render_template, request, redirect
from ..extensions import db
from ..models.post_form import PostForm

post_form = Blueprint('post_form', __name__)

@post_form.route('/post_form', methods = ['POST', 'GET'])
def create():
    if request.method == 'POST':
        
        post_form = PostForm(
            name=request.form.get('name'),
            attendance=request.form.get('attendance'),
            alcohol=','.join(request.form.getlist('alcohol')),
            song=request.form.get('song'),
            diet=request.form.get('diet')
        )
        try:
            db.session.add(post_form)
            db.session.commit()
        except Exception as e:
            print(str(e))
        return redirect('/post_form')
    else:
        return render_template('post_form/post_form.html')