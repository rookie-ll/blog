from app.froms import PostForm
from flask_login import current_user
from app.models import Posts, Users
from app.extends import db
from flask import flash, redirect, request, url_for, render_template, Blueprint

post_blue = Blueprint("post_blue", __name__, static_folder="../static", template_folder="../templates")


@post_blue.route('/postindex/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            u = current_user._get_current_object()
            post = Posts(
                content=form.conent.data,
                u_id=u.id
            )
            db.session.add(post)
            db.session.commit()
            flash("发表成功", "ok")
            return redirect(url_for("main.index"))
        else:
            flash("请先登陆后再评论", "登陆")
    page = request.args.get("page", 1, type=int)
    # posts = Posts.query.filter_by(rid=0).order_by(Posts.timestamp.desc()).all()
    page_data = Posts.query.filter_by(rid=0).join(
        Users
    ).order_by(Posts.timestamp.desc()).paginate(page=page, per_page=5, error_out=False)
    return render_template('posts/index.html', form=form, page_data=page_data)
