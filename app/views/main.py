from flask import render_template, redirect, url_for, flash, current_app, Blueprint
from flask_login import current_user
from flask_mail import Message
from werkzeug.security import check_password_hash, generate_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.extends import db
from app.froms import PostForm
from app.models import Posts

main = Blueprint('main', __name__, template_folder='../templeates')


@main.route('/', methods=['GET', 'POST'])
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
    posts = Posts.query.filter_by().order_by(Posts.timestamp.desc()).all()
    return render_template('main/index.html', form=form, posts=posts)


# 加密password
@main.route('/generate')
def generate():
    return generate_password_hash('123456')


# 解析password
@main.route('/check/<string:password>/')
def check(password):
    print(type(password))
    strs = "pbkdf2:sha256:150000$J61n8H2m$41ee8e3f54b6a0cbdaf7e77d6c1844e14c4bd8006e1a4c2a2ed8c854a4065417"
    if check_password_hash(strs, password):
        return "密码正确"
    else:
        return "密码错误"


# 生成token
@main.route('/generate_token/')
def generate_token():
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=3600)
    return s.dumps({"id": 500})


# 解析token
@main.route('/active/<string:token>/')
def actives(token):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=3600)
    try:
        data = s.loads(token)
    except:
        return "token 有误"
    return str(data.get("id"))


# 发送邮件
@main.route('/sed_mail/')
def sed_mail():
    app = current_app.__get__current_object()
